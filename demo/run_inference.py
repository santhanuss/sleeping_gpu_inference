from sleeping_gpu_inference.runtime.cpu_engine import run_cpu_inference
from sleeping_gpu_inference.runtime.gpu_engine import run_gpu_inference
from sleeping_gpu_inference.runtime.decision import decide_execution


def main():
    text = "Hello from Sleeping GPUs Inference Network"

    decision = decide_execution()
    print(f"🧠 SGIN Decision: {decision}")

    if decision == "GPU":
        result = run_gpu_inference(text)
    elif decision == "CPU":
        result = run_cpu_inference(text)
    else:
        print("⏸️ System busy or not energy-safe. Skipping inference.")
        return

    print("✅ Inference Result:")
    print(result)

if __name__ == "__main__":
    main()
