from __future__ import annotations

import csv
import socket
from collections import deque
from dataclasses import dataclass
from typing import Deque, Iterator, Optional


@dataclass(frozen=True)
class SampleRow:
    timestamp_ms: int
    voltage: float
    fault_label: str


class UdpReceiver:
    def __init__(self, host: str = "0.0.0.0", port: int = 5005, window_size: int = 50) -> None:
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((host, port))
        self.buffer: Deque[SampleRow] = deque(maxlen=window_size)
        self.window = self.buffer

    def read_row(self) -> Optional[SampleRow]:
        payload, _address = self.socket.recvfrom(4096)
        raw_line = payload.decode("utf-8", errors="replace").strip()
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

    def close(self) -> None:
        self.socket.close()
