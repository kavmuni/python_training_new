# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 15:28:30 2018

@author: calydon
"""

"""This program is used to get the 4th innings total"""

def sum_of_2_number(num_01, num_02):
    result=num_01+num_02
    return result

def diff_of_2_number(num_01, num_02):
    if num_01 > num_02:
        result=num_01 - num_02
    else:
        result=num_02 - num_01
    return result

def cricket_match():
    Aus1=int(input("Please input Aus1 value: "))
    Ind1=int(input("Please input Ind1 value: "))
    Aus2=int(input("Please input Aus2 value: "))
    Ind_inter=diff_of_2_number(Aus1,Ind1)
    Ind2=sum_of_2_number(Ind_inter,Aus2) + 1
    print("India need",str(Ind2),"to win the match")
    
def vegetables_values()    :
    vegetables=int(input("Please input vegetables value: "))
    fruits=int(input("Please input fruits value: "))
    amount_given=int(input("Please input amount_given value: "))
    total_fare=sum_of_2_number(vegetables,fruits)
    balance=diff_of_2_number(amount_given,total_fare)
    print("Shop keeper has to give ",str(balance),"balance")

def main():
    vegetables_values()

    
main()    