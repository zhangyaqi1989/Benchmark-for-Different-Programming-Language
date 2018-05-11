#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##################################
# University of Wisconsin-Madison
# Author: Yaqi Zhang
##################################
# run programs and measure times
##################################

from subprocess import call
import time
import socket
from collections import OrderedDict

def measure_time(command, n_times = 1):
    """run command n_times and compute the average time"""
    call(command) # for warm up
    start = time.time()
    for _ in range(n_times):
        call(command)
        # run(command)
    end = time.time()
    return (end - start) / n_times


def main(command_dic, outfile, n_times = 1):
    """main"""
    hostname = socket.gethostname()
    outfile = hostname + "-" + outfile
    with open(outfile, 'w') as out_file:
        for language, command in command_dic.items():
            print(command)
            time = measure_time(command, n_times)
            print(time)
            out_file.write("{}: {:.6f} s\n".format(language, time))


if __name__ == "__main__":
    command_dic = OrderedDict([
                   ("C++", ["./thermal_cpp"]),
                   ("Julia", ["julia", "thermal.jl"]),
                   ("C", ["./thermal_c"]),
                   ("Fortran", ["./thermal_f"]),
                   ("Java", ["java", "Thermal"]),
                   ("Python", ["python", "thermal_vec.py"]),
                   ("Javascript", ["node", "Javascript/thermal.js"]),
                   ("R", ["Rscript", "R/thermal.R"]),
                   ])
    main(command_dic, "times.txt", n_times = 2)
