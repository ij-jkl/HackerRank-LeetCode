""" https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true """

import cmath
# Read input
n = input()

#We assing to S the complex of N
s = complex(n)
#We show the absolute of s
print(abs(s))
# The phase angle
print(cmath.phase(s))