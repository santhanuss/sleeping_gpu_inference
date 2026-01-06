import csv
import os
from datetime import datetime

CSV_FILE = "sgin_metrics.csv"
HEADERS = [
    "timestamp",
    "decision",
    "energy_mWh",
    "carbon_gCO2",
    "plugged_in",
    "cpu_load",
    "gpu_available",
    "gpu_util",
    "gpu_temp",
]

def log_to_csv(state, decision, energy_mWh, carbon_gCO2):
    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(HEADERS)

        writer.writerow([
            datetime.now().isoformat(),
            decision,
            round(energy_mWh, 3),
            round(carbon_gCO2, 6),
            state.get("plugged_in"),
            state.get("cpu_load"),
            state.get("gpu_available"),
            state.get("gpu_util"),
            state.get("gpu_temp"),
        ])
