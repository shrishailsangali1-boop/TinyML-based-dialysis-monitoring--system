# ESP32-Based TinyML Dialysis Monitoring and Detection System

**Project type:** Academic prototype / engineering demonstration  
**Board:** ESP32  
**Sensors reported by the project team:** Turbidity, temperature, heart rate, and SpO₂  
**Output in this version:** ESP32 Serial Monitor (placeholder output interface)  
**ML status:** Random Forest offline training scaffold; TinyML deployment is **not yet implemented**.

> **Medical safety notice:** This is a student prototype, not a medical device. It must not be connected to a patient or dialysis machine, used to diagnose a condition, guide treatment, or make clinical decisions. Heart-rate and SpO₂ readings from hobby sensors are not clinical measurements. Use simulated or bench-test signals only, and obtain appropriate supervision for any hardware testing.

## 1. Project overview
The project explores collecting four categories of measurements using an ESP32:
- Turbidity sensor reading
- Temperature reading
- Heart-rate reading
- SpO₂ reading

The intended workflow is sensor acquisition → data logging → labelled dataset preparation → offline model training/evaluation → (future work) compact model conversion and embedded inference.

At present, the repository does **not** claim that a trained model is running on the ESP32. The supplied Python script is an offline Random Forest baseline only.

## 2. System block diagram
```text
Turbidity sensor ─┐
Temperature sensor ├──> ESP32 data acquisition
Heart-rate sensor ┤           |
SpO₂ sensor ──────┘           v
                       Serial Monitor / CSV logging
                                |
                                v
                     Labelled dataset (CSV)
                                |
                                v
                   Python Random Forest training
                                |
                                v
                    Evaluation metrics / model
                                |
                                v
                  Future work: TinyML conversion
                       and ESP32 inference
```

## 3. Hardware inventory (confirm exact models)
| Component | Project detail | Must be confirmed |
|---|---|---|
| Controller | ESP32 development board | Exact ESP32 variant |
| Turbidity | Turbidity sensor module | Model, output voltage, calibration |
| Temperature | Temperature sensor | Exact model and interface |
| Heart rate | Heart-rate sensor | Exact model |
| SpO₂ | Pulse-oximeter sensor | Exact model; many modules combine HR and SpO₂ |
| Output | Serial Monitor | Replace if another output is used |

**Important:** Do not connect a sensor output to an ESP32 pin until its voltage range is confirmed. ESP32 GPIOs are generally 3.3 V logic and are not 5 V tolerant. Use suitable level shifting/dividers where required. Confirm the board's ADC pin and sensor module requirements.

## 4. Repository structure
```text
tinyml-dialysis-monitoring-system/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── data/
│   ├── README.md
│   └── sample_schema.csv
├── docs/
│   ├── architecture.md
│   ├── hardware.md
│   ├── dataset.md
│   ├── model_training.md
│   └── results.md
├── firmware/
│   └── esp32_dialysis_monitor/
│       ├── esp32_dialysis_monitor.ino
│       └── README.md
├── models/
│   └── README.md
├── src/
│   └── train_model.py
└── results/
    └── README.md
```

## 5. Getting started: Python model baseline
Requirements: Python 3.10 or later.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

Prepare your own labelled dataset at `data/dialysis_dataset.csv`, following `data/README.md`, then run:

```bash
python src/train_model.py --data data/dialysis_dataset.csv --target status
```

The script trains and evaluates a Random Forest classifier, saves a local baseline model under `models/`, and writes evaluation metrics under `results/`. Dataset and generated model files are excluded from Git by default; only publish them if you have the right to share them and they contain no confidential information.

## 6. ESP32 firmware
Open `firmware/esp32_dialysis_monitor/esp32_dialysis_monitor.ino` in Arduino IDE, select the correct ESP32 board and port, then upload. The sketch is a **sensor integration scaffold**:
- Turbidity is read as a raw ADC value.
- Temperature, heart rate, and SpO₂ are placeholders until the exact sensor models and libraries are confirmed.
- Serial output is emitted as CSV-like rows.

Do not interpret placeholder `nan` values as measurements. Update pin numbers, calibration, sensor drivers, and units only after checking the actual modules and datasheets. The firmware does not perform ML inference.

## 7. TinyML implementation status
**Not yet implemented.** A future implementation should:
1. Validate the dataset and avoid data leakage.
2. Evaluate the model using appropriate class-wise metrics and an independent test set.
3. Select a deployment-compatible model and conversion path.
4. Measure model flash size, RAM use, and inference latency on the ESP32.
5. Test only in a controlled, non-clinical bench environment.

A scikit-learn Random Forest file is not automatically an ESP32 TinyML model. Do not claim TinyML deployment until conversion and on-device inference are completed and documented.

## 8. Results
Add only measurements from actual experiments. Report dataset source, number of samples, label definitions, train/test methodology, confusion matrix, precision, recall, F1-score, and limitations. Do not invent values or describe simulated data as real sensor measurements.

## 9. Future improvements
- Confirm and document exact sensor models and wiring.
- Add calibrated sensor drivers and robust error handling.
- Add a documented output interface (display, buzzer, app, etc.) if implemented.
- Collect a permitted, non-identifying dataset under appropriate supervision.
- Evaluate model robustness and class imbalance.
- Explore TinyML conversion and ESP32 inference as a separate milestone.

## 10. Contributors
- [Add student/team names]
- [Add guide, department, and institution if appropriate]

## License
MIT License; see `LICENSE`. Check third-party libraries and datasets for their own licences.
