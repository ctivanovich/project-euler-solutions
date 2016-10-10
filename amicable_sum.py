# -*- coding: utf-8 -*-
"""
Project Euler problem 21
"""


def amicable_num_sum(n):
    amicable = {i:[] for i in range(1,n)}
    for i in range(1,n):
        for j in range(1,i//2+1):
            if i%j==0:
                amicable[i].append(j)
                
    #checking if amicable, and rolling sum if so
    amicable_pairs_sum = 0
    amicable_pairs = []
    for num, divisors in amicable.items():
        #if sum of my values is a key in the dict, and sum of your values is me, we are amicable
        div_sum = sum(divisors)
        if div_sum in amicable and sum(amicable[div_sum]) == num and num!=div_sum:
                amicable_pairs_sum += num + div_sum
                amicable_pairs.append([num, div_sum])
        #divide amicable sum by 2, because of double-counting of pairs
    return (amicable_pairs, amicable_pairs_sum/2)
#n**2 + n run-time?