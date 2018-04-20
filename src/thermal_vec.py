#!/usr/bin/env python3
##################################
# University of Wisconsin-Madison
# Author: Yaqi Zhang
##################################
# simple thermal simulation
##################################

import numpy as np


def main(N):
    """thermal simulation"""
    DEPOSIT_T = 543.15
    max_temp = 0.0
    D = 0.004
    L = 0.005
    dt = 0.2
    RHO = 1050.0
    C = 2080.0
    PI = 3.1415926
    free_area = PI * D * L
    h = 75
    ENVELOP_T = 343.15
    e = 0.95
    S_B = 5.67e-8
    cross_area = PI * D * D / 4.0
    k = 0.177
    Ts = DEPOSIT_T * np.ones(N)
    Q_convs = np.zeros(N)
    Q_radis = np.zeros(N)
    Q_pres = np.zeros(N)
    Q_sucs = np.zeros(N)
    for i in range(N):
        # update temperature of i + 1 elements
        Q_convs[:i+1] = (Ts[:i+1] - ENVELOP_T) * free_area * h
        Q_radis[:i+1] = (Ts[:i+1]**4 - ENVELOP_T**4) * e * S_B * free_area
        Q_pres[1:i+1] = (Ts[1:i+1] - Ts[0:i]) * k * cross_area / L
        Q_sucs[0:i] = (Ts[0:i] - Ts[1:i+1]) * k * cross_area / L
        m = RHO * PI * D * D / 4 * L
        Ts[:i+1] = Ts[:i+1] - (Q_convs[:i+1] + Q_radis[:i+1] + Q_pres[:i+1] + Q_sucs[:i+1]) * dt / (m * C)
        if(Ts[0] > max_temp):
            max_temp = Ts[0]
    print("maxTemp = {:f}".format(max_temp))


if __name__ == "__main__":
    N = 40000
    main(N)
