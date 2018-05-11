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
import seaborn
seaborn.set()


if __name__ == "__main__":
    xticks = ['Julia', 'C', 'C++', 'Fortran', 'Java', 'CPython', 'NodeJS', 'R']
    i7_4870HQ_times = np.array([4.780, 3.693, 3.389, 2.591, 3.628, 32.015, 16.445, 130.351])
    i7_2600_times = np.array([7.093, 5.266, 5.010, 3.569, 10.458, 65.815, 138.833, 224.067])
    e5_times = np.array([5.505, 3.079, 3.033, 2.650, 6.076, 56.443, 8.131, 124.805])
    i7_6700_times = np.array([4.308, 2.370, 2.330, 2.017, 4.122, 71.302, 6.452, 202.943])
    n = len(xticks)
    ax = plt.axes()
    plt.scatter(np.arange(n), i7_4870HQ_times, color="orange", label="i7-4870HQ")
    plt.scatter(np.arange(n), i7_2600_times, color="red", label="i7-2600K")
    plt.scatter(np.arange(n), e5_times, color='blue', label="E5-2698")
    plt.scatter(np.arange(n), i7_6700_times, color="green", label="i7-6700")
    plt.xticks(np.arange(n), xticks)
    ax.set_yscale('log')
    plt.ylabel('time (s)')
    plt.legend(loc="upper left")
    plt.show()

