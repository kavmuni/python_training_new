# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 10:52:50 2018

@author: calydon
"""

from calc import sum, diff

vegetables=150
fruits=90
cash=500
total=sum(vegetables,fruits)
balance=diff(cash,total)

print("The balance amount is {bal}".format(bal=balance))