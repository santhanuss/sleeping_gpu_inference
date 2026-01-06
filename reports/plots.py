import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt

CSV_FILE = "sgin_metrics.csv"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "plots")


def load_data():
    timestamps = []
    energy = []
    carbon = []
    decisions = []

    with open(CSV_FILE, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            timestamps.append(datetime.fromisoformat(row["timestamp"]))
            energy.append(float(row["energy_mWh"]))
            carbon.append(float(row["carbon_gCO2"]))
            decisions.append(row["decision"])

    return timestamps, energy, carbon, decisions


def generate_plots():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    timestamps, energy, carbon, decisions = load_data()

    # Energy plot
    plt.figure()
    plt.plot(timestamps, energy)
    plt.xlabel("Time")
    plt.ylabel("Energy (mWh)")
    plt.title("SGIN Energy Usage Over Time")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "energy_over_time.png"))
    plt.close()

    # Carbon plot
    plt.figure()
    plt.plot(timestamps, carbon)
    plt.xlabel("Time")
    plt.ylabel("Carbon (gCO₂)")
    plt.title("SGIN Carbon Emissions Over Time")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "carbon_over_time.png"))
    plt.close()

    # Decision distribution
    cpu = decisions.count("CPU")
    gpu = decisions.count("GPU")
    skip = decisions.count("SKIP")

    plt.figure()
    plt.bar(["CPU", "GPU", "SKIP"], [cpu, gpu, skip])
    plt.xlabel("Decision")
    plt.ylabel("Count")
    plt.title("SGIN Decision Distribution")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "decision_distribution.png"))
    plt.close()
