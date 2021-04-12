# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 10:45:41 2021

@author: Miguel Correia
"""

import math
import numpy as np

x = np.deg2rad(30)
n = 0
N = 25
result = 0
sign = 1.0

while n < N:
    term = sign*x**(2*n)/math.factorial(2*n)
    result = result + term
    n +=1
    sign = -sign
print(result)
print((np.sqrt(3))/2)