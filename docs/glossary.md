# Technical Glossary

This glossary explains the main technical terms used in this project.

## System / HIL Terms

| Term                | Plain-English Meaning                                                           | In This Project                                                                                  |
| ------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| HIL                 | Hardware-in-the-loop. Real hardware is tested with a simulated physical system. | The Jetson processes data coming from a simulated circuit.                                       |
| HIL-inspired        | Similar to HIL, but not full industrial HIL yet.                                | Correct label for this project until real feedback from Jetson back to MATLAB/Simscape is added. |
| Simulation-to-edge  | A simulated system sends data to real edge hardware.                            | Simscape/MATLAB generates waveform data and sends it to the Jetson.                              |
| Virtual plant       | A simulated version of a physical system.                                       | The Simscape circuit model.                                                                      |
| Plant               | The system being modeled or controlled.                                         | The RC/op-amp filter circuit in Simscape.                                                        |
| Controller hardware | The real hardware that receives data and makes decisions.                       | The Jetson edge device.                                                                          |
| Closed loop         | Output from the hardware affects the simulation/input.                          | Future upgrade: Jetson detects a fault and sends a command back to MATLAB.                       |
| Open loop           | Data flows one way, without feedback.                                           | Current early version: Simscape sends waveform data to Jetson.                                   |
| Real-time           | Timing matters while the system runs.                                           | The project targets live-ish 100 Hz telemetry behavior.                                          |
| Testbed             | A controlled setup used to test ideas.                                          | The whole Simscape + UDP + Jetson + dashboard system.                                            |
| Diagnostic testbed  | A test setup that tries to find and explain problems.                           | The system detects waveform faults and reports what happened.                                    |

## MATLAB / Simulation Terms

| Term                | Plain-English Meaning                                            | In This Project                                                 |
| ------------------- | ---------------------------------------------------------------- | --------------------------------------------------------------- |
| MATLAB              | Engineering programming/math environment.                        | Used for scripts, data handling, UDP sending, and PDN modeling. |
| Simulink            | Block-diagram simulation environment from MathWorks.             | Optional environment for system-level simulation.               |
| Simscape            | MathWorks physical modeling tool.                                | Used to model physical electrical behavior.                     |
| Simscape Electrical | Simscape library for electrical systems.                         | Used to model the circuit/filter and power-delivery behavior.   |
| Circuit simulation  | Software-based testing of a circuit before building it.          | The circuit is tested virtually before hardware work.           |
| Model-based design  | Designing/testing with models before building physical hardware. | The circuit and PDN are modeled before real board work.         |
| Parameter           | A value you can change in a model.                               | R, C, cutoff frequency, voltage, load current.                  |
| Solver              | The simulation engine that calculates model behavior over time.  | Simscape uses a solver to compute waveform output.              |
| Scope               | A simulation viewer for signals.                                 | Used to view voltage waveforms.                                 |
| Export              | Save data from one tool into a file.                             | Save waveform data as CSV.                                      |
| CSV                 | Comma-separated values file.                                     | Stores waveform samples and logs.                               |

## Circuit / Signal Terms

| Term               | Plain-English Meaning                                                       | In This Project                                      |
| ------------------ | --------------------------------------------------------------------------- | ---------------------------------------------------- |
| Waveform           | A signal shape over time.                                                   | Voltage vs time from the simulated circuit.          |
| Voltage            | Electrical pressure/potential difference.                                   | The main measured signal.                            |
| Current            | Flow of electric charge.                                                    | Used in circuits and PDN modeling.                   |
| Resistance         | Opposition to current flow.                                                 | Used in RC filters and power-path modeling.          |
| Capacitance        | Ability to store charge/energy.                                             | Used in filters and decoupling networks.             |
| RC filter          | Resistor-capacitor filter.                                                  | Simple low-pass circuit model.                       |
| Low-pass filter    | Lets slow/low-frequency signals pass and weakens fast/high-frequency noise. | Main example circuit.                                |
| Active filter      | Filter using powered components like op-amps.                               | Possible upgraded Simscape model.                    |
| Op-amp             | Operational amplifier.                                                      | Used in active filter designs.                       |
| Cutoff frequency   | Frequency where a filter starts reducing signal strength.                   | One fault case shifts the cutoff frequency.          |
| Bode plot          | Graph showing how a circuit responds to frequency.                          | Used to show filter behavior.                        |
| Frequency response | How a system reacts to different frequencies.                               | Shows what frequencies the filter passes or weakens. |
| Noise              | Unwanted signal disturbance.                                                | One fault type.                                      |
| Noise burst        | Short period of strong noise.                                               | A simulated fault case.                              |
| Saturation         | Signal hits a limit and cannot increase normally.                           | Fault case where waveform may flatten.               |
| Clipping           | Top or bottom of waveform gets chopped flat.                                | Visible form of saturation.                          |
| Fault              | Intentional or abnormal problem condition.                                  | Noise burst, cutoff shift, saturation.               |
| Normal waveform    | Healthy expected signal.                                                    | Baseline signal for comparison.                      |
| Fault waveform     | Signal with a problem added.                                                | Used to test detection.                              |

## Telemetry / Networking Terms

| Term            | Plain-English Meaning                                                 | In This Project                                                               |
| --------------- | --------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| Telemetry       | Measurement data sent from one system to another.                     | Voltage samples sent from MATLAB to Jetson.                                   |
| UDP             | Fast network protocol that sends packets without guaranteed delivery. | Used to stream waveform data to the Jetson.                                   |
| Packet          | One small chunk of transmitted data.                                  | One sample message containing sequence number, timestamp, voltage, and label. |
| Port            | Network number used by software to receive/send data.                 | Python receiver listens on a UDP port.                                        |
| IP address      | Network address of a device.                                          | MATLAB sends packets to the Jetson IP.                                        |
| Socket          | Software endpoint for network communication.                          | Python and MATLAB use sockets/UDP interfaces.                                 |
| Sequence number | Packet counter.                                                       | Used to detect missing packets.                                               |
| Timestamp       | Time marker.                                                          | Used to measure timing and sample intervals.                                  |
| Sample          | One measured data point.                                              | One voltage value at a moment in time.                                        |
| Sample rate     | Samples per second.                                                   | Target is around 100 Hz.                                                      |
| 100 Hz          | 100 samples per second.                                               | Roughly one sample every 10 milliseconds.                                     |
| Packet loss     | Missing transmitted packets.                                          | Measured using skipped sequence numbers.                                      |
| Latency         | Delay between sending and receiving data.                             | Optional benchmark metric.                                                    |
| Throughput      | Amount of data moved over time.                                       | How much telemetry the pipeline can handle.                                   |

## Jetson / Edge Computing Terms

| Term                   | Plain-English Meaning                                               | In This Project                                     |
| ---------------------- | ------------------------------------------------------------------- | --------------------------------------------------- |
| Jetson                 | NVIDIA edge-AI computer family.                                     | The real edge device receiving and processing data. |
| Jetson Orin Nano Super | Specific NVIDIA edge-AI developer kit.                              | Target hardware for the project.                    |
| Edge device            | Local device that processes data near the source.                   | The Jetson.                                         |
| Edge computing         | Processing data locally instead of sending everything to the cloud. | The Jetson analyzes the waveform locally.           |
| Edge AI                | AI running locally on edge hardware.                                | Optional workload/classifier/reporting layer.       |
| Inference              | Running a trained AI model to get an output.                        | Optional Jetson workload to stress compute/power.   |
| Quantized model        | AI model compressed to lower precision.                             | Optional way to reduce RAM/compute usage.           |
| INT8                   | 8-bit integer format often used for efficient AI inference.         | Related to Jetson AI performance.                   |
| TOPS                   | Trillions of operations per second.                                 | Rough AI compute performance measure.               |
| RAM                    | Working memory.                                                     | Constraint for local AI and logs.                   |
| CPU                    | Central processor.                                                  | Handles general computing tasks.                    |
| GPU                    | Graphics/parallel processor.                                        | Helps accelerate AI and parallel workloads.         |
| Power mode             | Performance/power setting on the Jetson.                            | Used to compare normal vs heavier workloads.        |
| NVMe SSD               | Fast storage drive.                                                 | Useful for logs, models, and datasets.              |
| JetPack                | NVIDIA software stack for Jetson devices.                           | Operating environment/drivers/tools for Jetson.     |

## DSP / Detection Terms

| Term               | Plain-English Meaning                                    | In This Project                                    |
| ------------------ | -------------------------------------------------------- | -------------------------------------------------- |
| DSP                | Digital signal processing; math done on sampled signals. | Jetson filters and analyzes waveform data.         |
| Filter             | Method that changes or cleans a signal.                  | Used to smooth noisy voltage data.                 |
| EMA filter         | Exponential moving average filter.                       | Smooths voltage using current and previous values. |
| Feature            | Useful number extracted from raw data.                   | RMS, peak, mean, standard deviation, slope.        |
| Feature extraction | Turning raw samples into useful summary numbers.         | Used before fault detection.                       |
| RMS                | Root mean square; signal strength/energy measure.        | Helps detect abnormal amplitude.                   |
| Peak               | Highest signal value.                                    | Helps detect overvoltage/saturation.               |
| Mean               | Average value.                                           | Helps detect offset/bias.                          |
| Standard deviation | How spread out or noisy values are.                      | Helps detect noise bursts.                         |
| Slope              | How fast a signal changes.                               | Helps detect sudden jumps/glitches.                |
| Zero crossing      | When a signal crosses zero.                              | Can help estimate frequency behavior.              |
| Anomaly            | Something abnormal.                                      | A waveform behavior that does not look normal.     |
| Anomaly detection  | Detecting abnormal behavior.                             | Main fault-detection task.                         |
| Threshold          | A cutoff rule.                                           | Example: if peak is too high, flag fault.          |
| Threshold detector | Simple rule-based detector.                              | First anomaly detector.                            |
| Classifier         | System that labels data into categories.                 | Optional ML layer: normal/noise/cutoff/saturation. |
| Confusion matrix   | Table of correct vs incorrect classifications.           | Used to evaluate detector/classifier.              |
| False alarm        | Normal data incorrectly flagged as a fault.              | Important thing to measure.                        |
| Detection delay    | Time between fault happening and detector catching it.   | Benchmark metric.                                  |

## Dashboard / Diagnostics Terms

| Term              | Plain-English Meaning                       | In This Project                                          |
| ----------------- | ------------------------------------------- | -------------------------------------------------------- |
| Dashboard         | Visual screen showing system status.        | Shows voltage, packet rate, signal status, power status. |
| Visualization     | Displaying data visually.                   | Plots, dashboard, screenshots.                           |
| Diagnostic report | Short written explanation of what happened. | Output when a fault is detected.                         |
| Signal status     | Health of the waveform.                     | Normal, noise fault, cutoff shift, saturation.           |
| Power status      | Health of the power rail/PDN.               | Stable or droop warning.                                 |
| Benchmark         | Measured performance test.                  | Sample rate, packet loss, latency, CPU/RAM, droop.       |
| Benchmark logging | Saving benchmark results.                   | Stores proof that the system worked.                     |
| Runtime           | How long the system ran.                    | Final test should run long enough to be credible.        |
| Evidence          | Data supporting a diagnosis.                | Feature values, packet logs, plots.                      |

## PDN / Power Integrity Terms

| Term                 | Plain-English Meaning                                             | In This Project                                     |
| -------------------- | ----------------------------------------------------------------- | --------------------------------------------------- |
| PDN                  | Power delivery network.                                           | Path that delivers power to the Jetson.             |
| Power integrity      | Whether power stays stable and clean enough for hardware to work. | The PDN extension studies voltage droop under load. |
| Power rail           | Voltage supply line.                                              | Jetson input rail.                                  |
| 19V input            | 19-volt power input.                                              | Jetson developer kit power source.                  |
| Load                 | Device consuming power.                                           | Jetson acting as electrical load.                   |
| Load current         | Current demanded by the device.                                   | Increases during AI/DSP workload.                   |
| Current spike        | Sudden current increase.                                          | Happens when compute workload jumps.                |
| Voltage droop        | Voltage dip during load spike.                                    | Main PDN thing being studied.                       |
| Decoupling capacitor | Local energy buffer that helps stabilize voltage.                 | Used near load/output side.                         |
| Bulk capacitor       | Larger capacitor for bigger/slower energy changes.                | Used near input or power path.                      |
| Ceramic capacitor    | Small fast capacitor for high-frequency transients/noise.         | Used close to the load.                             |
| ESR                  | Equivalent series resistance.                                     | Unwanted resistance inside capacitor/model.         |
| ESL                  | Equivalent series inductance.                                     | Unwanted inductance inside capacitor/model.         |
| Cable resistance     | Resistance from wires/connectors.                                 | Modeled in PDN path.                                |
| Cable inductance     | Inductance from wires/connectors.                                 | Affects fast current changes.                       |
| TVS diode            | Transient voltage suppressor diode.                               | Protection part for voltage spikes.                 |
| Fuse                 | Overcurrent protection.                                           | Protects power path if something goes wrong.        |
| Polyfuse             | Resettable fuse.                                                  | Optional protection part.                           |
| Current sensor       | Part that measures current draw.                                  | Used to observe Jetson workload current.            |
| Voltage sense        | Measurement of voltage at a point.                                | Used to observe rail droop.                         |
| Test point           | Exposed measurement point on PCB.                                 | Lets you probe voltage/current/ground.              |
| Power interposer     | Small board placed between power supply and device.               | Realistic KiCad board concept.                      |
| Carrier board        | Board that hosts the Jetson module and interfaces.                | Not the summer MVP because it is much harder.       |

## KiCad / PCB Terms

| Term              | Plain-English Meaning                            | In This Project                             |
| ----------------- | ------------------------------------------------ | ------------------------------------------- |
| KiCad             | Free/open-source PCB design software.            | Used for PDN board concept.                 |
| PCB               | Printed circuit board.                           | Physical board layout.                      |
| Schematic         | Circuit drawing.                                 | First KiCad design step.                    |
| Schematic capture | Drawing the circuit in software.                 | Used before PCB layout.                     |
| PCB layout        | Physical arrangement of parts and copper traces. | Used after schematic.                       |
| Trace             | Copper path on PCB.                              | Carries power/signals.                      |
| Footprint         | Physical pad pattern for a component.            | Connects schematic part to PCB layout.      |
| Symbol            | Schematic representation of a component.         | Used in circuit diagram.                    |
| Net               | Electrical connection between points.            | Example: VIN, GND, VOUT.                    |
| Netlist           | List of circuit connections.                     | Connects schematic to layout.               |
| ERC               | Electrical rules check.                          | Finds schematic connection problems.        |
| DRC               | Design rules check.                              | Finds PCB layout rule problems.             |
| Ground pour       | Large copper area connected to ground.           | Helps power return path and noise behavior. |
| Connector         | Physical plug/header.                            | Input/output power connection.              |
| 3D render         | Visual model of the PCB.                         | Good portfolio screenshot.                  |
| Gerber files      | Manufacturing files for PCB fabrication.         | Optional if board is fabricated later.      |
| BOM               | Bill of materials.                               | List of parts needed for board.             |

## GitHub / Documentation Terms

| Term                   | Plain-English Meaning                       | In This Project                               |
| ---------------------- | ------------------------------------------- | --------------------------------------------- |
| Repository             | Project folder stored on GitHub.            | Main portfolio home.                          |
| README                 | Main front-page explanation file.           | Explains what the project does.               |
| Docs folder            | Folder for longer documentation.            | Holds architecture, glossary, protocol, logs. |
| Markdown               | Simple formatting language for GitHub docs. | `.md` files.                                  |
| Commit                 | Saved project checkpoint.                   | Shows progress history.                       |
| Branch                 | Separate development line.                  | Current branch is `main`.                     |
| License                | Legal permission rules for the code.        | MIT license used in repo.                     |
| Artifact               | Proof file.                                 | Screenshot, CSV, plot, benchmark, video.      |
| Build log              | Notes on what was built each session.       | Tracks progress and issues.                   |
| Architecture doc       | Document explaining system structure.       | `docs/architecture.md`.                       |
| Telemetry protocol doc | Document explaining packet format.          | `docs/telemetry_protocol.md`.                 |
| Glossary               | Dictionary of technical terms.              | This file.                                    |
| Topics                 | GitHub repo tags in the About sidebar.      | `matlab`, `simscape`, `jetson`, `dsp`, etc.   |

## File / Repo Terms

| Term         | Plain-English Meaning               | In This Project                                         |
| ------------ | ----------------------------------- | ------------------------------------------------------- |
| `README.md`  | Main project explanation.           | Front page of repo.                                     |
| `docs/`      | Documentation folder.               | Architecture, glossary, logs, protocol.                 |
| `matlab/`    | MATLAB scripts/models folder.       | UDP sender and Simscape-related files.                  |
| `src/`       | Source code folder.                 | Python receiver, DSP, dashboard.                        |
| `data/`      | Input/generated data folder.        | Sample waveforms and logs.                              |
| `results/`   | Output results folder.              | Plots, benchmark tables, reports.                       |
| `kicad/`     | KiCad design folder.                | PDN interposer board files.                             |
| `.gitignore` | File telling Git what not to track. | Prevents junk/temp files from being committed.          |
| `.md`        | Markdown file extension.            | Correct extension for GitHub docs.                      |
| `.txt`       | Plain text file extension.          | Not ideal for Markdown docs. Rename `.md.txt` to `.md`. |

## One-Sentence Project Explanation

This project is a HIL-inspired edge diagnostic testbed where Simscape generates simulated circuit-fault waveforms, MATLAB streams them over UDP to a Jetson edge device, Python performs DSP filtering and anomaly detection, and a dashboard/report shows signal health, timing benchmarks, and optional PDN/KiCad power-integrity validation.
