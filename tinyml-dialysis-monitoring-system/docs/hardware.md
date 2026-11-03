# Hardware and Wiring

| Component | Exact module/model | Interface | ESP32 pin | Status |
|---|---|---|---|---|
| ESP32 | [Fill exact board] | — | — | Board selected |
| Turbidity sensor | [Fill model] | Analog / digital | GPIO 34 placeholder | Pin must be verified |
| Temperature sensor | [Fill model] | [Fill] | [Fill] | Driver not added |
| Heart-rate sensor | [Fill model] | [Fill] | [Fill] | Driver not added |
| SpO₂ sensor | [Fill model] | [Fill] | [Fill] | Driver not added |
| Output | Serial Monitor | USB serial | USB | Scaffold output |

## Electrical safety and integration notes
- Verify the exact ESP32 board pinout before wiring.
- ESP32 GPIO uses 3.3 V logic; do not apply 5 V to GPIO/ADC pins.
- Confirm sensor module supply voltage and output voltage from its datasheet.
- Add appropriate level shifting or a voltage divider if required.
- Confirm ADC attenuation, resolution, calibration, and sensor transfer function.
- Many optical pulse-oximeter modules estimate heart rate and SpO₂ together; confirm the exact module and library.
- Do not connect this prototype to a patient or dialysis equipment.
