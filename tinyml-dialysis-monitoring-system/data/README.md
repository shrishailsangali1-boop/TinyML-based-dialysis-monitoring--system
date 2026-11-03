# Dataset

Place your own labelled file here as `dialysis_dataset.csv`. Never upload identifiable patient data, confidential clinical records, or data you do not have permission to share.

## Required columns for the supplied training script
- `turbidity_raw` — raw ADC or documented calibrated turbidity value (state units and calibration)
- `temperature_c` — temperature in degrees Celsius
- `heart_rate_bpm` — beats per minute
- `spo2_percent` — percentage
- `status` — target class label, for example `normal` / `abnormal`, **only if these labels are defined and justified by your project protocol**

The script uses numeric feature columns and the target column. Missing sensor readings must be handled transparently; do not fill them with invented values.

## Data provenance
Document whether each row is bench-measured, simulated, or from a permitted public dataset. Record sensor model, calibration, sampling interval, test conditions, label-generation method, and dataset licence. Do not use patient data for this academic prototype.
