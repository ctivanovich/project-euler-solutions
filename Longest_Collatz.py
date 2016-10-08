# -*- coding: utf-8 -*-
"""
Created on Thu May  5 10:50:50 2016

@author: Christopher
"""



"""
n → n/2 (n is even)
n → 3n + 1 (n is odd)

"""
from time import time

def Collatz(start):
    chain_length = 0
    term = start
    while term != 1:
        if term%2==0:
            term = term/2
        else:
            term = 3*term + 1
        chain_length += 1
    return chain_length
    
timestart = time()

start = 2
new_length = 0
old_length = 0
collatz_num = 0
while start < 10000000:
    new_length = Collatz(start)
    if old_length < new_length:
        old_length = new_length
        collatz_num = start
    start += 1
    
print(old_length)
print(collatz_num)
print(time()-timestart)