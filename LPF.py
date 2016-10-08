# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 16:06:32 2015
Largest Prime Factor Algorithm
@author: Christopher
"""
import time
def is_prime(a):
    if a%2==0:
        return False
    for i in range(2, int(a/2)+1):
        if a % i == 0 and a!=2:
            return False    
    return True

primes = []

def lpf(num, lo):
    
    global primes
    hi = num
    for i in range((lo), int(hi)+1):
        
        if num%i == 0:
            if is_prime(i):
                primes.append(i)
                return lpf(num/i, i)
    return primes
start = time.time()
print(lpf(600851475143,2))
print(time.time()-start)