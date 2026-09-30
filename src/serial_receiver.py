# Reads the Arduino's ms,volts,label lines off USB serial into a rolling buffer.
import argparse
import csv
from collections import deque, namedtuple

import serial

SampleRow = namedtuple("SampleRow", "timestamp_ms voltage fault_label")


class SerialReceiver:
    def __init__(self, port, baudrate=115200, window_size=50, timeout=1.0):
        self.serial = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)
        self.buffer = deque(maxlen=window_size)

    def read_row(self):
        line = self.serial.readline().decode("utf-8", errors="replace").strip()
        # opening the port resets the Uno, so the first line or two are often junk
        try:
            t, v, label = next(csv.reader([line]))[:3]
            sample = SampleRow(int(t), float(v), label.strip())
        except (csv.Error, ValueError):
            return None
        self.buffer.append(sample)
        return sample

    def read_forever(self):
        while True:
            sample = self.read_row()
            if sample is not None:
                yield sample

    def latest_window(self):
        return tuple(self.buffer)

    def voltages(self):
        return [s.voltage for s in self.buffer]

    def timestamps_ms(self):
        return [s.timestamp_ms for s in self.buffer]

    def labels(self):
        return [s.fault_label for s in self.buffer]

    def close(self):
        self.serial.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("port")
    parser.add_argument("--baudrate", type=int, default=115200)
    parser.add_argument("--window-size", type=int, default=50)
    args = parser.parse_args()

    rx = SerialReceiver(args.port, args.baudrate, args.window_size)
    try:
        for s in rx.read_forever():
            print(s)
    except KeyboardInterrupt:
        pass
    rx.close()
