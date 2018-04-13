#!/usr/bin/env python3
##################################
# University of Wisconsin-Madison
# Author: Yaqi Zhang
##################################
# simple thermal simulation
##################################

import numpy as np


def compute_conv(T, D, L):
    """compute convection"""
    PI = 3.1415926
    area = PI * D * L
    h = 75
    ENVELOP_T = 343.15
    return h * area * (T - ENVELOP_T)


def compute_radi(T, D, L):
    """compute radiation"""
    PI = 3.1415926
    area = PI * D * L
    e = 0.95
    S_B = 5.67e-8
    E_T = 343.15
    return e * S_B * area * (T * T * T * T - E_T * E_T * E_T * E_T)


def compute_inter(T1, T2, D, L):
    """compute conduction"""
    PI = 3.1415926
    area = PI * D * D / 4.0
    k = 0.177
    return k * area / L * (T1 - T2)


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
    Ts = DEPOSIT_T * np.ones(N)
    temp_Ts = np.zeros(N)
    for i in range(N):
        for j in range(i + 1):
            Q_conv = compute_conv(Ts[j], D, L)
            Q_radi = compute_radi(Ts[j], D, L)
            Q_pre = compute_inter(Ts[j], Ts[j - 1], D, L) if j > 0 else 0
            Q_suc = compute_inter(Ts[j], Ts[j + 1], D, L) if j < i else 0
            m = RHO * PI * D * D / 4 * L
            temp_Ts[j] = Ts[j] - (Q_conv + Q_radi + Q_pre + Q_suc) * dt / (m * C)
        for j in range(i + 1):
            Ts[j] = temp_Ts[j]
        if(Ts[0] > max_temp):
            max_temp = Ts[0]
    print("maxTemp = {:f}".format(max_temp))


if __name__ == "__main__":
    N = 40
    main(N)
