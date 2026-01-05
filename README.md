💤 Sleeping GPU Inference Network (SGIN)



Wake sleeping GPUs. Not data centers.



SGIN is an energy-aware, user-side AI inference framework that intelligently decides where inference should run — CPU, GPU, or not at all — based on real hardware conditions.



Instead of defaulting to cloud inference, SGIN reuses idle (“sleeping”) user compute to reduce energy waste, preserve privacy, and slow unnecessary data-center expansion.



🌍 Why SGIN?



Modern AI systems rely heavily on cloud infrastructure:



Always-on GPUs



High cooling and network energy



Rising costs and carbon footprint



Meanwhile, millions of user devices sit idle for most of the day.



SGIN flips the model:



Move inference to the user’s compute — only when it is safe and efficient.



🚀 Key Features



🔋 Energy-aware decision engine

Chooses CPU, GPU, or SKIP based on:



Power state (plugged in / battery)



CPU load



GPU availability \& temperature



😴 Sleeping GPU logic

Uses GPU only if already awake — avoids unnecessary wake-ups.



🧠 Policy-driven execution

Decisions are rule-based, transparent, and configurable.



🔐 Local-first \& privacy-preserving

No data leaves the device by default.



🧩 Extensible architecture

Ready for logging, scheduling, ONNX models, GPU acceleration, and future hybrid compute.



🧪 Quick Demo



Run the demo from the repository root:



python -m sleeping\_gpu\_inference.demo.run\_inference



Example output:

🧠 SGIN Decision: CPU

🖥️ Running inference on CPU

✅ Inference Result:

\[CPU RESULT] Hello from Sleeping GPUs Inference Network





Depending on system conditions, SGIN may choose:



GPU



CPU



SKIP (system busy or energy-unsafe)



All outcomes are correct behavior.



📁 Project Structure

sleeping\_gpu\_inference/

├── demo/

│   └── run\_inference.py      # Demo runner

├── profiler/

│   └── hardware\_state.py     # CPU/GPU state detection

├── runtime/

│   ├── cpu\_engine.py         # CPU inference engine

│   ├── gpu\_engine.py         # GPU inference engine

│   └── decision.py           # Execution decision logic

├── .gitignore

├── \_\_init\_\_.py

└── README.md



🧠 How the Decision Works



SGIN evaluates system conditions before inference:



Condition	Action

GPU idle, cool, plugged in	Run on GPU

On battery or GPU too warm	Run on CPU

High system load	Skip inference



This ensures responsible compute usage, not brute force execution.



🌱 Environmental Impact



SGIN helps reduce:



Data-center GPU demand



Network energy usage



Idle hardware waste



Always-on compute patterns



It promotes event-driven, energy-aware AI, aligned with Green IT and ESG goals.



🛠️ Installation

git clone https://github.com/santhanuss/sleeping\_gpu\_inference.git

cd sleeping\_gpu\_inference

python -m pip install psutil





(Additional runtimes like ONNX can be added later.)



🛣️ Roadmap



&nbsp;Real ONNX model integration



&nbsp;Decision \& energy logging



&nbsp;Night-time / scheduled inference



&nbsp;GPU acceleration support



&nbsp;Cloud fallback comparison



&nbsp;Research \& whitepaper version



🤝 Contributing



Contributions are welcome — especially around:



Green AI



Edge inference



Scheduling \& metrics



Distributed / hybrid compute



Open an issue or pull request to start.



📄 License



MIT License



👤 Author



Santhanu

GitHub: https://github.com/santhanuss



Building sustainable, energy-aware AI systems.💤 Sleeping GPU Inference Network (SGIN)



Wake sleeping GPUs. Not data centers.



SGIN is an energy-aware, user-side AI inference framework that intelligently decides where inference should run — CPU, GPU, or not at all — based on real hardware conditions.



Instead of defaulting to cloud inference, SGIN reuses idle (“sleeping”) user compute to reduce energy waste, preserve privacy, and slow unnecessary data-center expansion.



🌍 Why SGIN?



Modern AI systems rely heavily on cloud infrastructure:



Always-on GPUs



High cooling and network energy



Rising costs and carbon footprint



Meanwhile, millions of user devices sit idle for most of the day.



SGIN flips the model:



Move inference to the user’s compute — only when it is safe and efficient.



🚀 Key Features



🔋 Energy-aware decision engine

Chooses CPU, GPU, or SKIP based on:



Power state (plugged in / battery)



CPU load



GPU availability \& temperature



😴 Sleeping GPU logic

Uses GPU only if already awake — avoids unnecessary wake-ups.



🧠 Policy-driven execution

Decisions are rule-based, transparent, and configurable.



🔐 Local-first \& privacy-preserving

No data leaves the device by default.



🧩 Extensible architecture

Ready for logging, scheduling, ONNX models, GPU acceleration, and future hybrid compute.



🧪 Quick Demo



Run the demo from the repository root:



python -m sleeping\_gpu\_inference.demo.run\_inference



Example output:

🧠 SGIN Decision: CPU

🖥️ Running inference on CPU

✅ Inference Result:

\[CPU RESULT] Hello from Sleeping GPUs Inference Network





Depending on system conditions, SGIN may choose:



GPU



CPU



SKIP (system busy or energy-unsafe)



All outcomes are correct behavior.



📁 Project Structure

sleeping\_gpu\_inference/

├── demo/

│   └── run\_inference.py      # Demo runner

├── profiler/

│   └── hardware\_state.py     # CPU/GPU state detection

├── runtime/

│   ├── cpu\_engine.py         # CPU inference engine

│   ├── gpu\_engine.py         # GPU inference engine

│   └── decision.py           # Execution decision logic

├── .gitignore

├── \_\_init\_\_.py

└── README.md



🧠 How the Decision Works



SGIN evaluates system conditions before inference:



Condition	Action

GPU idle, cool, plugged in	Run on GPU

On battery or GPU too warm	Run on CPU

High system load	Skip inference



This ensures responsible compute usage, not brute force execution.



🌱 Environmental Impact



SGIN helps reduce:



Data-center GPU demand



Network energy usage



Idle hardware waste



Always-on compute patterns



It promotes event-driven, energy-aware AI, aligned with Green IT and ESG goals.



🛠️ Installation

git clone https://github.com/santhanuss/sleeping\_gpu\_inference.git

cd sleeping\_gpu\_inference

python -m pip install psutil





(Additional runtimes like ONNX can be added later.)



🛣️ Roadmap



&nbsp;Real ONNX model integration



&nbsp;Decision \& energy logging



&nbsp;Night-time / scheduled inference



&nbsp;GPU acceleration support



&nbsp;Cloud fallback comparison



&nbsp;Research \& whitepaper version



🤝 Contributing



Contributions are welcome — especially around:



Green AI



Edge inference



Scheduling \& metrics



Distributed / hybrid compute



Open an issue or pull request to start.



📄 License



MIT License



👤 Author



Santhanu

GitHub: https://github.com/santhanuss



Building sustainable, energy-aware AI systems.

