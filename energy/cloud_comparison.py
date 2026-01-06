# Cloud vs SGIN energy & carbon comparison

# Cloud assumptions
CLOUD_GPU_POWER_W = 250       # Datacenter GPU
INFERENCE_TIME_S = 0.5
CARBON_INTENSITY = 475        # gCO2 per kWh


def cloud_energy_per_run_wh():
    return (CLOUD_GPU_POWER_W * INFERENCE_TIME_S) / 3600


def cloud_carbon_per_run_g():
    energy_kwh = cloud_energy_per_run_wh() / 1000
    return energy_kwh * CARBON_INTENSITY


def compare_cloud_vs_sgin(sgin_energy_mWh, sgin_carbon_g, runs):
    cloud_energy_wh = cloud_energy_per_run_wh() * runs
    cloud_carbon_g = cloud_carbon_per_run_g() * runs

    return {
        "runs": runs,
        "sgin_energy_mWh": round(sgin_energy_mWh, 2),
        "sgin_carbon_g": round(sgin_carbon_g, 4),
        "cloud_energy_Wh": round(cloud_energy_wh, 2),
        "cloud_carbon_g": round(cloud_carbon_g, 4),
        "carbon_saved_g": round(cloud_carbon_g - sgin_carbon_g, 4),
    }
