# Simple, conservative energy & carbon estimates

# Average power draw (Watts) during short inference
CPU_POWER_W = 15      # typical laptop CPU burst
GPU_POWER_W = 60      # mobile / low-power GPU burst

# Average inference duration (seconds)
INFERENCE_TIME_S = 0.5

# Carbon intensity (gCO2 per kWh)
# Global average ≈ 475 gCO2/kWh
CARBON_INTENSITY = 475


def estimate_energy_wh(power_w, time_s):
    return (power_w * time_s) / 3600


def estimate_carbon_g(energy_wh):
    energy_kwh = energy_wh / 1000
    return energy_kwh * CARBON_INTENSITY


def estimate_impact(decision):
    if decision == "CPU":
        energy = estimate_energy_wh(CPU_POWER_W, INFERENCE_TIME_S)
    elif decision == "GPU":
        energy = estimate_energy_wh(GPU_POWER_W, INFERENCE_TIME_S)
    else:  # SKIP
        energy = 0.0

    carbon = estimate_carbon_g(energy)
    return energy, carbon
