import onnxruntime as ort
import numpy as np
import os

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "..", "models", "mnist.onnx"
)

def run_onnx_cpu_inference():
    session = ort.InferenceSession(
        MODEL_PATH,
        providers=["CPUExecutionProvider"]
    )

    input_name = session.get_inputs()[0].name

    # MNIST expects (1, 1, 28, 28)
    dummy_input = np.random.rand(1, 1, 28, 28).astype("float32")

    outputs = session.run(None, {input_name: dummy_input})
    prediction = int(np.argmax(outputs[0]))

    return f"[ONNX CPU] Prediction: {prediction}"
