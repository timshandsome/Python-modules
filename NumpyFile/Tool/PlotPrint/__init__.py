import numpy as np
import time
import matplotlib.pyplot as plt

class PLOT_FIGURE():
    def __init__(self, r_file, traceset, ptrace, vrange):
        self.r_file = r_file
        self.traceset = traceset
        self.ptrace = ptrace
        self.vrange = vrange

    def plot_data(self, path):
        plt.figure(1)
        for p_trace in range(self.ptrace):
            plt.title(self.r_file)
            plt.plot(self.traceset[self.ptrace])
            plt.axis([0, self.traceset.shape[1], -self.vrange, self.vrange])
            plt.grid(alpha=0.3)
        figure = plt.gcf()
        figure.patch.set_facecolor('white')
        figure.set_size_inches(15, 6)
        plt.savefig(f"{path}/{self.r_file}.png")
        # plt.show()

class PRINT_DATA():
    def __init__(self, traceset, dataset):
        self.traceset = traceset
        self.dataset = dataset

    def set_data(self, trim_traceset, trim_dataset):
        self.traceset = trim_traceset
        self.dataset = trim_dataset

    def print_data(self):
        print('Traceset:\n', self.traceset)
        print('Dataset :\n', self.dataset)

