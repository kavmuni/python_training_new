# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 10:13:55 2018

@author: calydon
"""
arr=[-10,0,10]
print(type(arr))
print(arr)
arr_set=set(arr)
arr=list(arr_set)
arr.sort()
print(arr)
print(arr[-2])