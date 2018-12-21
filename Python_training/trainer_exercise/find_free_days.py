# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 16:28:22 2018

@author: calydon
"""

def find_free_days():
    free_days=list()
    full_month=list(range(1,31))
    #print(full_month)
    booked=[1,3,9,12,13,18,26,27,28,29]
    holiday=[4,5,15,16,21,22]
    occupied=booked+holiday
    #for item in full_month:
        #if item not in occupied:
            #free_days.append(item)
    free_days=[item for item in full_month if item not in occupied]        
    free_days.sort()        
    print(free_days) 

def main():
    find_free_days()

if __name__=='__main__':
    main()         
    
    