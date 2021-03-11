import numpy as np
import matplotlib.pyplot as plt

class Transform:
    def __init__(self, plot_xrange, plot_yrange, n_points):
        self.plot_xrange = plot_xrange
        self.plot_yrange = plot_yrange
        self.n_points = n_points
        self.x = None
        self.y = None

    def plot(self, save=False, name=None):
        plt.xlim(self.plot_xrange)
        plt.ylim(self.plot_yrange)
        plot = plt.plot(self.x, self.y)

        if save:
            if name:
                plt.savefig(name)
            else:
                raise RuntimeError('Specify name')

        return plot

    def fft(self, save=False, name=None):
        sp = np.fft.fft(self.y)
        freq = np.fft.fftfreq(self.x.shape[-1])
        plt.xlim(self.plot_xrange)
        plt.ylim(self.plot_yrange)
        plot = plt.plot(freq, sp.real, freq, sp.imag)

        if save:
            if name:
                plt.savefig(name)
            else:
                raise RuntimeError('Specify name')

        return plot