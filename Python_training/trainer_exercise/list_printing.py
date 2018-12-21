# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 15:49:16 2018

@author: calydon
"""

def list_printing():
    num_list=[1,5,6,3,4,5,8,9,0,3]
    num_list.sort()
    for number in num_list:
        print(number)
        
def main():
    list_printing()        
    
if __name__=='__main__':
    main()    