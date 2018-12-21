# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 12:30:33 2018

@author: calydon
"""
captain_names_append=[]
FH="captains.txt"
with open(FH) as MYFILE:
        for line in MYFILE:
            each_line=line.split(',')
            #print(each_line)
            if each_line[0] != "Player":
                captain_names=each_line[0]
                #print(captain_names)#ceptain name
                captain_names_append.append(captain_names)
print("-------------------------")      
for name in captain_names_append[:6]:
    print(name,end=",")#first 5 captain name  
print("\n-------------------------") 
for name in captain_names_append[-5:]:#last 5 captain name
    print(name, end=",")

