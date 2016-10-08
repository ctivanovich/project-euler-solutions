# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 12:06:30 2015

@author: Christopher
"""

def smallest(factor):
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    j = 0
    while True:
        j += 1
        for i in range(1, factor+1):
            if j%i == 0:
                if i == factor:
                     return i, j, j/i
                continue
            else:
                break
       
#        if j > 100000000:
#            raise Exception("Too many iterations")
print(smallest(20))