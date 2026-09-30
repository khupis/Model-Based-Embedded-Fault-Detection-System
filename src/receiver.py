# Same ms,volts,label rows as serial_receiver.py, but one per UDP datagram.
import csv
import socket
from collections import deque, namedtuple

SampleRow = namedtuple("SampleRow", "timestamp_ms voltage fault_label")


class UdpReceiver:
    def __init__(self, host="0.0.0.0", port=5005, window_size=50):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((host, port))
        self.buffer = deque(maxlen=window_size)

    def read_row(self):
        payload, _ = self.socket.recvfrom(4096)
        line = payload.decode("utf-8", errors="replace").strip()
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

    def close(self):
        self.socket.close()
