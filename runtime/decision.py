from sleeping_gpu_inference.profiler.hardware_state import hardware_state


def decide_execution():
    state = hardware_state()

    if not state["plugged_in"]:
        return "CPU"

    if state["gpu_available"]:
        if state["gpu_util"] is not None and state["gpu_temp"] is not None:
            if state["gpu_util"] < 30 and state["gpu_temp"] < 75:
                return "GPU"

    if state["cpu_load"] < 70:
        return "CPU"

    return "SKIP"
