# -*- coding: utf-8 -*-
"""
Created on Thu May 12 16:51:43 2016

@author: Christopher
"""

from num2words import num2words
sum = 0
for i in range(1,1001):
    
    word = num2words(i, ordinal=False)
    word = word.strip()
    sum += len(word)
    for e in word:
        if e ==" " or e == "-":
            sum-=1
print(sum)