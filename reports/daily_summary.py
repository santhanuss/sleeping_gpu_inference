import csv
from datetime import date
from sleeping_gpu_inference.energy.cloud_comparison import compare_cloud_vs_sgin

CSV_FILE = "sgin_metrics.csv"

def generate_daily_summary(target_date=None):
    if target_date is None:
        target_date = date.today().isoformat()

    total_runs = 0
    cpu_runs = 0
    gpu_runs = 0
    skip_runs = 0
    total_energy = 0.0
    total_carbon = 0.0

    with open(CSV_FILE, newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if not row["timestamp"].startswith(target_date):
                continue

            total_runs += 1
            decision = row["decision"]

            if decision == "CPU":
                cpu_runs += 1
            elif decision == "GPU":
                gpu_runs += 1
            else:
                skip_runs += 1

            total_energy += float(row["energy_mWh"])
            total_carbon += float(row["carbon_gCO2"])

    return {
        "date": target_date,
        "total_runs": total_runs,
        "cpu_runs": cpu_runs,
        "gpu_runs": gpu_runs,
        "skip_runs": skip_runs,
        "energy_mWh": round(total_energy, 2),
        "carbon_gCO2": round(total_carbon, 4),
    }

def print_daily_summary(summary):
    print("\n📅 SGIN Daily Summary")
    print(f"Date: {summary['date']}")
    print(f"Total runs: {summary['total_runs']}")
    print(f"CPU runs: {summary['cpu_runs']}")
    print(f"GPU runs: {summary['gpu_runs']}")
    print(f"Skipped runs: {summary['skip_runs']}")
    print(f"⚡ Total SGIN energy: {summary['energy_mWh']} mWh")
    print(f"🌍 Total SGIN carbon: {summary['carbon_gCO2']} gCO₂")

    comparison = compare_cloud_vs_sgin(
        summary["energy_mWh"],
        summary["carbon_gCO2"],
        summary["total_runs"]
    )

    print("\n☁️ Cloud Comparison (same workload)")
    print(f"⚡ Cloud energy: {comparison['cloud_energy_Wh']} Wh")
    print(f"🌍 Cloud carbon: {comparison['cloud_carbon_g']} gCO₂")
    print(f"🌱 Carbon saved by SGIN: {comparison['carbon_saved_g']} gCO₂")
