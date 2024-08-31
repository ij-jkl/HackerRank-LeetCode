""" https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true """

#!/bin/python3

import math
import os
import random
import re
import sys


def solve(s):
    for i in s.split():
        s = s.replace(i, i.capitalize())
    return s


if __name__ == '__main__':


    s = input()

    result = solve(s)
