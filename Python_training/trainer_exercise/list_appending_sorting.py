# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 15:54:13 2018

@author: calydon
"""
def list_appending_sorting():
    list_appended= list()
    FH="numbers.txt"
    with open(FH) as MYFILE:
        for line in MYFILE:
            #each_line=line
            #print(each_line)
            list_elements=line
            list_appended.append(int(list_elements))
    print(list_appended)        
    print("-------------------------")      
    for num in list_appended:
        print(num)
    print("\n-------------------------") 
    list_appended.sort(reverse=False)
    for num in list_appended:
        print(num)
        
def main():
    list_appending_sorting()

if __name__=='__main__':
    main()            