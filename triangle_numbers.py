# -*- coding: utf-8 -*-
"""
Created on Wed May  4 11:21:24 2016

@author: Christopher
"""
from math import sqrt
def is_prime(a):
    for i in range(2, int(a**.5)+1):
        if a % i == 0:
            return False    
    return True


def countPFactors(number):
    pfactors = []
    for i in range(2,number//2+1):
        if is_prime(i):
            if not number%i:
                pfactors.append(i)
    return pfactors

def triangleNumbers(n):
    return(int((n*(n+1)/2)))
    
from time import time

def NumberOfDivisors(number):
    divisors = 0
    tworoot = sqrt(number);
    for i in range(1, int(tworoot)+1):
        if number%i==0:
            divisors += 2   
#    //Correction if the number is a perfect square
    if (sqrt*sqrt == number):
        divisors-=1
    return divisors
    
#number = 0
#i=1
#timestart = time()
#while NumberOfDivisors(number) < 500:
#    number += i
#    i+=1
#print(number)
#print(time()-timestart)
