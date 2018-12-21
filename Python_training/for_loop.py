# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 16:29:13 2018

@author: calydon
"""

for num in range(94,109):
    if len(str(num)) == 2:
        num = num/2
        print(num)
    else:
        print(num * 2)
        