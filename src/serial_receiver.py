from __future__ import annotations

import csv
from collections import deque
from dataclasses import dataclass
from typing import Deque, Iterator, Optional

import serial


@dataclass(frozen=True)
class SampleRow:
    timestamp_ms: int
    voltage: float
    fault_label: str


class SerialReceiver:
    def __init__(
        self,
        port: str,
        baudrate: int = 115200,
        window_size: int = 50,
        timeout: float = 1.0,
    ) -> None:
        self.serial = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)
        self.buffer: Deque[SampleRow] = deque(maxlen=window_size)
        self.window = self.buffer

    def read_row(self) -> Optional[SampleRow]:
        raw_line = self.serial.readline().decode("utf-8", errors="replace").strip()
        if not raw_line:
            return None

        try:
            row = next(csv.reader([raw_line]))
        except csv.Error:
            return None

        if len(row) < 3:
            return None

        try:
            sample = SampleRow(
                timestamp_ms=int(row[0]),
                voltage=float(row[1]),
                fault_label=row[2].strip(),
            )
        except ValueError:
            return None

        self.buffer.append(sample)
        return sample

    def read_forever(self) -> Iterator[SampleRow]:
        while True:
            sample = self.read_row()
            if sample is not None:
                yield sample

    def latest_window(self) -> tuple[SampleRow, ...]:
        return tuple(self.buffer)

    def voltages(self) -> list[float]:
        return [sample.voltage for sample in self.buffer]

    def timestamps_ms(self) -> list[int]:
        return [sample.timestamp_ms for sample in self.buffer]

    def labels(self) -> list[str]:
        return [sample.fault_label for sample in self.buffer]

    def close(self) -> None:
        self.serial.close()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Read Arduino CSV telemetry over USB serial.")
    parser.add_argument("port")
    parser.add_argument("--baudrate", type=int, default=115200)
    parser.add_argument("--window-size", type=int, default=50)
    args = parser.parse_args()

    receiver = SerialReceiver(args.port, baudrate=args.baudrate, window_size=args.window_size)
    try:
        for sample in receiver.read_forever():
            print(sample)
    except KeyboardInterrupt:
        pass
    finally:
        receiver.close()
