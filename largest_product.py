# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 13:35:15 2016

@author: Christopher
"""

for i in range(1001):
    
    for j in range(i, 1001):
        
        for k in range (j, 1001):
            if i*i + j*j == k*k:
                if i + j + k == 1000:
                    print(i,j,k)