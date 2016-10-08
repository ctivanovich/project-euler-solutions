# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 16:36:03 2016

@author: Christopher
"""
import math
probs = [.2,  .2,   0,   0,   0,   0,  .9,  .1,  .1,  .1,  .3,   0, .1,  .6,  0,   0,   0,   0,   0,  .4,  .1,  .2,  .4,  .6, 0,   0,   1,   1,  .9,  .9,  .1,   0,   0,   0,   0,   0, .7,  .2,   0,   0,  .1,  .1,   0,  .5,  .8,  .7,  .3,  .4]
for i in range(12):
    try:
        -1*(probs[i]*math.log(probs[i],2)+
        probs[12+i]*math.log(probs[12+i],2)+
        probs[i+24]*math.log(probs[i+24],2)+
        probs[i+36]*math.log(probs[i+36],2))
    except ValueError:
        continue