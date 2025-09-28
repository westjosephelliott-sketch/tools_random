import threading
import time

import numpy as np


class Anomaly_Core:
    def __init__(self, window=50, sensitivity=3.0):
        self.window = window
        self.sensitivity = sensitivity
        self.buffer = []
        self.lock = threading.Lock()

    def ingest(self, value):
        with self.lock:
            self.buffer.append(value)
            if len(self.buffer) > self.window:
                self.buffer.pop(0)

    def detect(self):
        if len(self.buffer) < self.window:
            return False
        x = np.array(self.buffer)
        μ = np.mean(x)
        σ = np.std(x)
        latest = x[-1]
        return abs(latest - μ) > self.sensitivity * σ

    def stream(self, source):
        for value in source:
            self.ingest(value)
            if self.detect():
                print(f"⚠️ anomaly: {value}")
            time.sleep(0.05)

            def generator():
                while True:
                    yield np.random.normal(0, 1) if np.random.rand() > 0.05 else np.random.normal(10, 1)

            if __name__ == "__main__":
                core = Anomaly_Core(window=60, sensitivity=2.5)
                core.stream(generator())