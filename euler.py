# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 20:29:03 2015

@author: ci381
"""

#Largest prime factor
#Problem 3
#The prime factors of 13195 are 5, 7, 13 and 29.
#
#What is the largest prime factor of the number 600851475143 ?

#Problem 3 Largest Prime Factor

from time import time
 
def largest_prime_factor(n):
 
    largest_factor = 1
 
    # remove any factors of 2 first
    while n % 2 == 0:
        largest_factor = 2
        n = n//2
 
    # now look at odd factors
    p = 3
    while n != 1:
        while n % p == 0:
            largest_factor = p
            n = n//p
        p += 2
 
    return largest_factor
 
start = time()
a = largest_prime_factor(600851475143)
elapsed = (time() - start)
 
print(a, elapsed)