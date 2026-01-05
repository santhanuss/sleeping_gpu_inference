&nbsp;💤 Sleeping GPU Inference Network (SGIN)



\*\*Energy-aware AI inference that knows when \*not\* to run.\*\*



SGIN is a local-first inference framework that decides \*\*CPU / GPU / SKIP\*\*

based on time, hardware state, and energy impact — helping reduce unnecessary

compute, cost, and carbon emissions.



---



\## 🌍 Why SGIN?



Most AI systems assume:

> \*Inference must always run.\*



SGIN asks a better question:

> \*\*Should inference run right now?\*\*



By respecting \*\*time windows\*\*, \*\*hardware conditions\*\*, and \*\*energy impact\*\*,

SGIN avoids waste and promotes sustainable AI execution.



---



\## ✨ Key Capabilities



\- 🧠 \*\*Policy-driven decisions\*\*: CPU, GPU, or SKIP  

\- 🌙 \*\*Time-aware scheduling\*\* (work-life \& power policies)

\- 🔋 \*\*Energy estimation\*\* (mWh)

\- 🌱 \*\*Carbon estimation\*\* (gCO₂)

\- 📊 \*\*CSV telemetry \& daily summaries\*\*

\- 📈 \*\*Auto-generated plots\*\*

\- ☁️ \*\*Cloud vs local carbon comparison\*\*



---



\## 🧪 Quick Start



Run inference with decision logic:



```bash

python -m sleeping\_gpu\_inference.demo.run\_inference

Run daily summary:



bash

Copy code

python -m sleeping\_gpu\_inference.demo.run\_daily\_summary

Generate plots:



bash

Copy code

python -m sleeping\_gpu\_inference.demo.run\_plots

📁 Project Structure

bash

Copy code

sleeping\_gpu\_inference/

├── demo/          # Runnable entry points

├── runtime/       # CPU / GPU execution engines

├── profiler/      # Hardware state detection

├── scheduler/     # Time-based policies

├── energy/        # Energy \& carbon estimation

├── logging/       # CSV \& decision logs

├── reports/       # Summaries \& plots

├── plots/         # Generated PNG graphs

└── README.md

🧠 How Decisions Work

SGIN evaluates, in order:



⏰ Time policy (allowed window?)



🔌 Power state (plugged in?)



🎮 GPU state (idle \& cool?)



🖥️ CPU load



❌ Otherwise → SKIP



Skipping inference is treated as a valid, optimal decision.



📊 Metrics \& Visuals

SGIN generates plots directly from real execution data.



🔋 Energy Usage Over Time



🌍 Carbon Emissions Over Time



🧠 Decision Distribution



☁️ Cloud vs SGIN (Why Local Wins)

For the same workload:



Cloud inference uses always-on datacenter GPUs



SGIN runs only when needed



SKIP = zero energy, zero carbon



Daily reports quantify carbon saved by avoiding cloud inference.



🌱 Design Philosophy

Prefer not running over running inefficiently



Use estimates, not fake precision



Optimize for policy \& behavior, not benchmarks



Make sustainability measurable



🛣️ Roadmap

YAML-based policy configuration



Weekly / monthly reports



Cloud vs SGIN overlay graphs



GPU acceleration path



Blog / whitepaper version



🤝 Contributing

Ideas, issues, and discussions are welcome.

This project is about better decisions, not bigger models.



📄 License

MIT License



👤 Author

Santhanu

GitHub: https://github.com/santhanuss



Building thoughtful, energy-aware AI systems.

