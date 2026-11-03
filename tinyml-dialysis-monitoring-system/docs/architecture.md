# System Architecture

## Current implemented scope
The ESP32 firmware scaffold reads a raw analog turbidity input and prints a row to the Serial Monitor. Temperature, heart-rate, and SpO₂ fields remain placeholders until exact sensor models and driver libraries are confirmed. Offline Random Forest training is provided in Python. TinyML inference on the ESP32 is not implemented.

## Data flow
1. Sensor modules produce electrical signals or digital measurements.
2. ESP32 acquires readings using the appropriate interface.
3. Serial Monitor provides a development output stream.
4. Measurements are logged and curated into a labelled CSV dataset.
5. Python trains and evaluates an offline Random Forest baseline.
6. Future work may convert a suitable model and implement inference on the ESP32.

## Future embedded inference
Document the conversion tool, model format, feature ordering, preprocessing implementation, memory footprint, and measured inference latency. Verify numerical parity between desktop and embedded predictions before making performance claims.
