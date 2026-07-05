# fault_bench_shield

KiCad project plan for a 2-layer Arduino Uno shield that supports the planned next-stage hardware for the fault detection bench.

## Board Goal

Build a compact sensor front-end called `fault_bench_shield` that conditions the plant signal for the Arduino Uno, injects controlled faults, and passes ERC and DRC with zero errors before fabrication.

## Functional Blocks

The planned shield includes a 1 kΩ / 1 µF RC plant, an MCP6001 op-amp voltage-follower buffer on the A0 sense line, a 5 V relay used as a noise-burst fault injector, a jumper-selectable 3 kΩ resistor for the cutoff-shift fault, four test points, and female headers for the Uno.

## Layer Stack

Top layer: signal routing.

Bottom layer: continuous GND pour.

## Parts And Footprints

| Part | Value / Package | Notes |
| --- | --- | --- |
| Op-amp | MCP6001, SOT-23-5 | Voltage follower buffer on the sense line. |
| Resistor | 1 kΩ, 0805 | RC plant resistor. |
| Capacitor | 1 µF, 0805 | RC plant capacitor. |
| Resistor | 3 kΩ, jumper-selectable, 0805 | Used to shift the cutoff fault case. |
| Relay | 5 V relay | Noise-burst fault injector. |
| Headers | 1x15 female headers | Mate with the Arduino Uno shield footprint. |

## Layout Rules

Keep the A0 sense path short, route the buffered output cleanly, and place the relay away from the analog front-end to reduce coupling. Use the bottom GND pour to improve return current paths and shield the measurement trace.

## Verification

Target a clean schematic and board flow where ERC reports zero electrical rule errors and DRC reports zero layout errors before export.

## Fabrication

Fabricate at JLCPCB as a 2-layer board. The rough target cost is about $20 for a small prototype run, depending on shipping and assembly choices.
