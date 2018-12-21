# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 12:17:14 2018

@author: calydon
"""

file_content=open(r'C:\Python_training\trainer_exercise\captains.txt')
first_10_line=file_content.read(10)
first_20_line=file_content.read(20)
print(first_10_line)
print(first_20_line)
print("10th character is:",first_10_line[-1:])
file_content.close()
print("--------------------------------------------------------")
file_content=open(r"C:\Python_training\trainer_exercise\captains.txt")
first_20_line=file_content.read(20)
rest_of_line=file_content.read()
appended_string=first_20_line+'good'+rest_of_line
print(appended_string)
file_content.close()
