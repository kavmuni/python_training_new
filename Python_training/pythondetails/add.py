# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 19:28:21 2018

@author: Muniappan
"""

def add(num_01=0,num_02=0):
    result=num_01+num_02
    return result

def main():
    print("The result of add without parameters is ", str(add()))
    print("The result of add with 1 parameters is ", str(add(1)))
    print("The result of add with 2 parameters is ", str(add(1,1)))
    
main()    