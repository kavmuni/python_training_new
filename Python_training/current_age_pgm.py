# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 12:07:11 2018

@author: calydon
"""
import datetime as dt
current_date=dt.datetime.now()
current_year=current_date.year
print("current_year: "+str(current_year))
input_year=input("Please input your birth year: ")
age=current_year - int(input_year) + 10
print("YOur age 10 years from now is "+ str(age))