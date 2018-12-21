# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 10:46:21 2018

@author: calydon
"""

def sum(num_01,num_02):
    result=num_01 + num_02
    return result

def diff(num_01,num_02):
    result=num_01 - num_02
    return result

def main():
    x=20
    y=10
    result_01=sum(x,y)
    result_02=diff(x,y)
    print(result_01)
    print(result_02)

if __name__=="__main__":
    main()