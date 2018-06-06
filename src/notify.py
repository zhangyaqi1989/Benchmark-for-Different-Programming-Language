#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##################################
# University of Wisconsin-Madison
# Author: Yaqi Zhang
##################################
"""
This module contains a notify function
"""

# standard library
import sys
from subprocess import call

# third party library
import itchat


if __name__ == "__main__":
    _, *commands = sys.argv
    itchat.auto_login()
    print(commands)
    call(commands)
    msg = "{} finished".format(' '.join(commands))
    itchat.send(msg, toUserName='filehelper')
