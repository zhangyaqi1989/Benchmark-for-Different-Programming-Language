#!/usr/bin/env python3
##################################
# University of Wisconsin-Madison
# Author: Yaqi Zhang
##################################
# compare running time
##################################

import numpy as np
import matplotlib.pyplot as plt
plt.style.use("seaborn")
# import seaborn
# seaborn.set()


if __name__ == "__main__":
    i7_2600_times = [5.014, 3.405, 5.860, 62.517]
    e5_times = [3.012, 2.632, 4.887, 55.174]
    i7_6700_times = [2.403, 13.615, 4.032, 60.159]
    xticks = ['C', 'Fortran', 'Julia', 'Python']
    n = len(xticks)
    plt.scatter(np.arange(n), i7_2600_times, color="red", label="i7-2600K")
    plt.scatter(np.arange(n), e5_times, color='blue', label="E5-2698")
    plt.scatter(np.arange(n), i7_6700_times, color="green", label="i7-6700")
    plt.xticks(np.arange(n), xticks)
    plt.ylabel('time (s)')
    plt.legend(loc="upper left")
    plt.show()

