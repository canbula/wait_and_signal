import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib


class AnimatedHist:
    def __init__(self):
        matplotlib.use("TkAgg")
        self.fig, self.axs = plt.subplots(1, 2, tight_layout=True)

    def init(self):
        self.axs[0].bar([0, 1, 2, 3], [10, 4, 25, 5])
        self.axs[1].bar([0, 1, 2, 3], [2, 4, 5, 2])

    def update(self, frame):
        print(frame)
        self.axs[1].bar([0, 1, 2, 3], [10, 10, 10, 10])

    def draw(self):
        ani = FuncAnimation(self.fig, self.update, init_func=self.init)
        plt.show()


animated_hist = AnimatedHist()
animated_hist.draw()

