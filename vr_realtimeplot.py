import threading
import time
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from ubicoders_vrobots import System, GeneralRobot

class RealtimePlot:
    def __init__(self, max_entries=100, ylabels=None, title=None):
        self.max_entries = max_entries
        self.ts_data = []
        self.y_data = []
        self.ylabels = ylabels  # list of y-axis labels
        self.title = title
        self.thread = threading.Thread(target=self.init_plot, daemon=True)
        self.thread.start()

    def init_plot(self):
        self.figure, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [], 'r-')        
        self.ax.set_xlabel('Time (s)')
        self.ax.set_title(self.title)
        self.ax.set_ylabel(self.ylabels)
        ani = animation.FuncAnimation(self.figure, self.update_plot, interval=100)
        plt.show()

    def update(self, ts, theta_dot):
        self.ts_data.append(ts)
        self.y_data.append(theta_dot)
        if len(self.ts_data) > self.max_entries:
            self.ts_data.pop(0)
            self.y_data.pop(0)

    def update_plot(self, frame):
        if self.ts_data:
            self.line.set_data(self.ts_data, self.y_data)
            self.ax.set_ylim(min(self.y_data)-10, max(self.y_data)+10)
            self.ax.set_xlim(min(self.ts_data), max(self.ts_data) + 1)
            self.ax.figure.canvas.draw()