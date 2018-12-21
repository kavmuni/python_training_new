# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 10:50:34 2018

@author: calydon
"""

from calc import sum, diff

aus1=250
ind1=190
aus2=100

total=sum(aus1,aus2)
ind2=diff(total,ind1)

print("India need {} to win the match".format(ind2+1))