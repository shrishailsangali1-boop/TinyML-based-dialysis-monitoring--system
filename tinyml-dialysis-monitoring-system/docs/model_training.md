# Random Forest Baseline

The Python script `src/train_model.py` trains a scikit-learn Random Forest classifier from a labelled CSV file.

## Run
```bash
pip install -r requirements.txt
python src/train_model.py --data data/dialysis_dataset.csv --target status
```

## Important distinction
This is offline model development, not TinyML deployment. The saved `.joblib` pipeline is intended for Python and is not directly executable as ESP32 firmware. TinyML work remains future work until a supported conversion/deployment approach and on-device inference are implemented and measured.

## Evaluation
Report class-wise precision, recall and F1-score, confusion matrix, dataset size, class balance, and split method. Accuracy alone may hide poor performance on a minority class.
