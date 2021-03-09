import numpy as np
import matplotlib.pyplot as plt

class Transform:
    def __init__(self):
        self.x = None
        self.y = None

    def plot(self, name):
        plt.plot(self.x, self.y)
        plt.savefig(name)

    def fft(self, name):
        sp = np.fft.fft(self.y)
        freq = np.fft.fftfreq(self.x.shape[-1])
        plt.plot(freq, sp.real, freq, sp.imag)
        plt.savefig(name)