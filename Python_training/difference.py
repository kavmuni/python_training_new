# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 15:20:11 2018

@author: calydon
"""

"""This function is to add 2 input values"""

def diff_of_2_number():
    num_01=int(input("Please input 1st number: "))
    num_02=int(input("Please input 2nd number: "))
    if num_01 > num_02:
        result=num_01 - num_02
    else:
        result=num_02 - num_01
    return result

def main():
    print_result=diff_of_2_number()
    print("THe difference between 2 numbers is ", str(print_result))
    
main()    