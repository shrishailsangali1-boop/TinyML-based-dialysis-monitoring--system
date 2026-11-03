"""Train an offline Random Forest baseline from a labelled CSV.

Example:
  python src/train_model.py --data data/dialysis_dataset.csv --target status
This does not convert or deploy a TinyML model to the ESP32.
"""
from pathlib import Path
import argparse
import json
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

EXPECTED_FEATURES = [
    "turbidity_raw",
    "temperature_c",
    "heart_rate_bpm",
    "spo2_percent",
]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="data/dialysis_dataset.csv")
    parser.add_argument("--target", default="status")
    parser.add_argument("--test-size", type=float, default=0.2)
    parser.add_argument("--random-state", type=int, default=42)
    args = parser.parse_args()

    path = Path(args.data)
    if not path.exists():
        raise SystemExit(
            f"Dataset not found: {path}. Prepare your own labelled CSV; see data/README.md."
        )

    df = pd.read_csv(path)
    if args.target not in df.columns:
        raise SystemExit(f"Target column '{args.target}' is missing.")

    missing = [c for c in EXPECTED_FEATURES if c not in df.columns]
    if missing:
        raise SystemExit(f"Missing expected feature columns: {missing}")

    X = df[EXPECTED_FEATURES].apply(pd.to_numeric, errors="coerce")
    y = df[args.target]
    if y.isna().any():
        raise SystemExit("Target labels contain missing values.")
    if y.nunique() < 2:
        raise SystemExit("At least two target classes are required.")
    if X.isna().all(axis=1).any():
        raise SystemExit("At least one row has no usable sensor features; review the dataset.")

    stratify = y if y.value_counts().min() >= 2 else None
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=args.test_size, random_state=args.random_state,
        stratify=stratify
    )

    pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("classifier", RandomForestClassifier(
            n_estimators=100, random_state=args.random_state,
            class_weight="balanced"
        ))
    ])
    pipeline.fit(X_train, y_train)
    pred = pipeline.predict(X_test)

    accuracy = accuracy_score(y_test, pred)
    report_dict = classification_report(y_test, pred, output_dict=True, zero_division=0)
    matrix = confusion_matrix(y_test, pred)

    print("Features:", EXPECTED_FEATURES)
    print(f"Offline test accuracy: {accuracy:.4f}")
    print(classification_report(y_test, pred, zero_division=0))
    print("Confusion matrix:\\n", matrix)

    Path("models").mkdir(exist_ok=True)
    Path("results").mkdir(exist_ok=True)
    joblib.dump(
        {"pipeline": pipeline, "feature_names": EXPECTED_FEATURES, "target_name": args.target},
        "models/random_forest_baseline.joblib"
    )
    summary = {
        "accuracy": accuracy,
        "features": EXPECTED_FEATURES,
        "target": args.target,
        "classes": [str(c) for c in pipeline.named_steps["classifier"].classes_],
        "confusion_matrix": matrix.tolist(),
        "classification_report": report_dict,
        "status": "offline baseline only; TinyML deployment not implemented",
        "medical_note": "Not validated for clinical use; not for patient monitoring or treatment decisions."
    }
    Path("results/evaluation.json").write_text(json.dumps(summary, indent=2))
    print("Saved offline baseline model and evaluation metrics.")

if __name__ == "__main__":
    main()
