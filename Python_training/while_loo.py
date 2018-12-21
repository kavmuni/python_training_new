# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 16:27:07 2018

@author: calydon
"""

a=0
while a<10:
    print(a)
    a += 1
print("----------------------------")    
for num in [1,2,3,4,5]:
    if num % 2 == 0:
        continue
    print(num)
print("----------------------------") 
for num in [1,2,3,4,5]:
    if num % 2 == 0:
        break
    print(num)
print("----------------------------") 
for num in [1,2,3,4,5]:
    if num % 2 == 0:
        pass
    print(num)       