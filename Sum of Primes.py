# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 15:05:19 2016

@author: Christopher
"""
total = 2

def is_prime(a):
    for i in range(2, int(a**.5)+1):
        if a % i == 0:
            return False    
    return True

for i in range(3,2000001):
    if i%2:
        if is_prime(i):
            total += i
print(total)