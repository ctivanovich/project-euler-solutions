# -*- coding: utf-8 -*-
"""
Created on Thu May  5 10:29:16 2016

@author: Christopher
"""

with open("C:\\Users\\Christopher\\OneDrive\\Code\\Project Euler\\giant_sum.txt") as f:
    file = f.read()
    data = file.split()
    f.close()

sum = 0

for num in data:
    sum+=int(num)
sum = str(sum)
print(sum[-1:10])