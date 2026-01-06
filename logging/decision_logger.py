from datetime import datetime
import json
import os

LOG_FILE = "sgin_decisions.log"

def log_decision(state, decision):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "decision": decision,
        "plugged_in": state.get("plugged_in"),
        "cpu_load": state.get("cpu_load"),
        "gpu_available": state.get("gpu_available"),
        "gpu_util": state.get("gpu_util"),
        "gpu_temp": state.get("gpu_temp"),
    }

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(log_entry) + "\n")
