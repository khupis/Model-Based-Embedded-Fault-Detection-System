# Architecture Overview

This project is a real-hardware fault detection bench. The physical circuit is the source of truth, and the Simscape model is used as a digital twin to validate the hardware behavior and fault logic.

## System Flow

```mermaid
flowchart LR
	A[Physical Plant\nBreadboard RC/RLC circuit] --> B[Arduino Uno\nADC @ 100 Hz]
	B --> C[Python serial receiver]
	C --> D[DSP pipeline]
	D --> E[Dashboard / results]
	F[Simscape digital twin] -. validates .-> A
	G[Stateflow FSM] -. fault logic .-> D
	H[KiCad 2-layer sensor front-end] -. supports .-> A
```

## Role Of Each Block

The physical plant is the actual circuit under test, built on breadboard and later mirrored on a custom shield/front-end. The Arduino Uno samples the plant through its ADC at roughly 100 Hz and streams timestamped CSV rows over USB serial.

The Python serial receiver is the handoff point into software. It maintains a rolling sample buffer, feeds the DSP filters, and provides the data window used by feature extraction and anomaly detection.

The DSP pipeline consumes the live buffer, extracts features, and classifies the three fault cases injected into the bench. The dashboard and results layer records the traces, detections, and runtime evidence.

The Simscape digital twin mirrors the circuit so the hardware measurements can be validated against a modeled reference. It is not the primary signal source.

## Data Flow Diagram

Physical Plant (breadboard) -> Arduino Uno (ADC, 100 Hz) -> Python serial receiver -> DSP pipeline -> dashboard/results

## Validation Strategy

The digital twin is used to compare expected versus measured behavior, tune fault thresholds, and document design intent. Hardware results are considered the authoritative benchmark, with the model serving as a controlled reference.
