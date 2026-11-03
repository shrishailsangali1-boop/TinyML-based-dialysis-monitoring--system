# Dataset Collection and Labelling Protocol

Create a data dictionary for every feature: exact sensor, units, calibration method, sampling frequency, valid range, and missing-value representation.

## Suggested columns
`turbidity_raw`, `temperature_c`, `heart_rate_bpm`, `spo2_percent`, `status`

## Labelling
Define what `normal` and `abnormal` mean for the specific **non-clinical bench experiment**. Labels must come from a documented test protocol, not arbitrary thresholds or medical assumptions. Do not use this model to identify clinical abnormalities.

## Quality controls
- Exclude personally identifying or confidential information.
- Record sensor faults and missing readings rather than fabricating values.
- Keep repeated measurements from the same test condition together when splitting data to reduce leakage.
- Keep a final test set separate from model development.
- Document whether data is simulated, bench-measured, or public.
