# ESP32 Firmware Scaffold

Open `esp32_dialysis_monitor.ino` in Arduino IDE and install the ESP32 board package. Select your exact board and serial port.

The sketch currently reads one analog turbidity input and prints a CSV header and rows. Temperature, heart-rate and SpO₂ are output as `nan` placeholders. This is intentional: the exact sensor models have not yet been provided, so no sensor driver is guessed.

Before using:
1. Confirm exact ESP32 board and pinout.
2. Confirm each sensor module model and datasheet.
3. Verify supply and output voltage compatibility.
4. Implement and test each sensor driver separately.
5. Add calibration and unit conversion.
6. Keep all testing non-clinical and off-patient.
