import psutil
import subprocess

def is_plugged_in():
    battery = psutil.sensors_battery()
    return battery.power_plugged if battery else True

def cpu_load():
    return psutil.cpu_percent(interval=1)

def gpu_available():
    try:
        subprocess.check_output(["nvidia-smi"], stderr=subprocess.DEVNULL)
        return True
    except Exception:
        return False

def gpu_utilization():
    try:
        output = subprocess.check_output(
            ["nvidia-smi",
             "--query-gpu=utilization.gpu,temperature.gpu",
             "--format=csv,noheader,nounits"]
        ).decode().strip()
        util, temp = map(int, output.split(","))
        return util, temp
    except Exception:
        return None, None

def hardware_state():
    state = {
        "plugged_in": is_plugged_in(),
        "cpu_load": cpu_load(),
        "gpu_available": gpu_available(),
        "gpu_util": None,
        "gpu_temp": None
    }

    if state["gpu_available"]:
        util, temp = gpu_utilization()
        state["gpu_util"] = util
        state["gpu_temp"] = temp

    return state
