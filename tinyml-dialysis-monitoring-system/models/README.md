# Models

TinyML deployment is not implemented yet.

The training script can create a local scikit-learn `.joblib` baseline after a real labelled dataset is supplied. This file is not an ESP32-ready model. For future deployment, choose and document a supported conversion/runtime path, implement identical preprocessing on-device, and measure flash, RAM, and inference time. Do not commit private data or model files trained on data you are not permitted to share.
