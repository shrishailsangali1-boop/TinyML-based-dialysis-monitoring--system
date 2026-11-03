# TinyML-based-dialysis-monitoring--system
embedded and iot project
ESP32-Based TinyML Dialysis Monitoring and Detection System
Project type: Academic prototype / engineering demonstration
Board: ESP32
Sensors reported by the project team: Turbidity, temperature, heart rate, and SpO₂
Output in this version: ESP32 Serial Monitor (placeholder output interface)
ML status: Random Forest offline training scaffold; TinyML deployment is not yet implemented.

Medical safety notice: This is a student prototype, not a medical device. It must not be connected to a patient or dialysis machine, used to diagnose a condition, guide treatment, or make clinical decisions. Heart-rate and SpO₂ readings from hobby sensors are not clinical measurements. Use simulated or bench-test signals only, and obtain appropriate supervision for any hardware testing.

1. Project overview
The project explores collecting four categories of measurements using an ESP32:

Turbidity sensor reading
Temperature reading
Heart-rate reading
SpO₂ reading
The intended workflow is sensor acquisition → data logging → labelled dataset preparation → offline model training/evaluation → (future work) compact model conversion and embedded inference.

At present, the repository does not claim that a trained model is running on the ESP32. The supplied Python script is an offline Random Forest baseline only.

2. System block diagram
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
3. Hardware inventory (confirm exact models)
Component	Project detail	Must be confirmed
Controller	ESP32 development board	Exact ESP32 variant
Turbidity	Turbidity sensor module	Model, output voltage, calibration
Temperature	Temperature sensor	Exact model and interface
Heart rate	Heart-rate sensor	Exact model
SpO₂	Pulse-oximeter sensor	Exact model; many modules combine HR and SpO₂
Output	Serial Monitor	Replace if another output is used
Important: Do not connect a sensor output to an ESP32 pin until its voltage range is confirmed. ESP32 GPIOs are generally 3.3 V logic and are not 5 V tolerant. Use suitable level shifting/dividers where required. Confirm the board's ADC pin and sensor module requirements.

