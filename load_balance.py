import random
import time
from threading import Thread, Condition
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib
import numpy as np


matplotlib.use("TkAgg")


class JobsAndUsers:
    def __init__(self, number_of_users, number_of_resources, job_size):
        self.n = number_of_users
        self.r = number_of_resources
        self.m = job_size
        self.resources = [Condition() for _ in range(number_of_resources)]
        self.jobs = [job_size for _ in range(number_of_users)]
        self.queue = [0 for _ in range(number_of_resources)]

    def user(self, i):
        print("Hi, I am user #%d" % i)
        while self.jobs[i] > 0:
            time.sleep(3 + random.random())
            print("User #%d wants to start now" % i)
            r = self.queue.index(min(self.queue))
            self.queue[r] += 1
            print("User #%d is trying to get the resource #%d" % (i, r))
            if self.resources[r].acquire():
                print("User #%d has the resource #%d" % (i, r))
                time.sleep(5 + random.random())
                self.jobs[i] -= 1
                self.queue[r] -= 1
                self.resources[r].notify()
                self.resources[r].release()
                print("User #%d has completed the job" % i)
            else:
                print("User #%d could not get the resource #%d" % (i, r))


def prepare_animation(bar_container):

    def animate(frame_number):
        # simulate new data coming in
        data = np.random.randn(1000)
        n, _ = np.histogram(data, np.linspace(-4, 4, 100))
        for count, rect in zip(n, bar_container.patches):
            rect.set_height(count)
        return bar_container.patches
    return animate


def main():
    n = 10
    r = 3
    m = 100
    jobs_and_users = JobsAndUsers(n, r, m)
    users = [Thread(target=jobs_and_users.user, args=(i,)) for i in range(n)]
    for user in users:
        user.start()
    HIST_BINS = np.linspace(-4, 4, 100)
    data = np.random.randn(1000)
    n, _ = np.histogram(data, HIST_BINS)
    fig, ax = plt.subplots()
    _, _, bar_container = ax.hist(data, HIST_BINS, lw=1,
                                  ec="yellow", fc="green", alpha=0.5)
    ax.set_ylim(top=55)
    ani = animation.FuncAnimation(fig, prepare_animation(bar_container), 50,
                                  repeat=False, blit=True)
    plt.show()
    for user in users:
        user.join()


if __name__ == "__main__":
    main()
