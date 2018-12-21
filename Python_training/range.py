# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 17:04:41 2018

@author: calydon
"""

some=range(4)
more=range(10,14)
for values in [*some,*more]:
    if values > 10:
        break
    else:
        print(values + 10)