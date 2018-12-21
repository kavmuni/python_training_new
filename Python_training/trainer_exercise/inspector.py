# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 13:41:05 2018

@author: calydon
"""

import sys as sys

def inspector():
    starting_line=1
    ending_line=5
    count=starting_line
    file_name="captains.txt"
    if len(sys.argv) >= 3:
        if sys.argv[1] != " ":
            starting_line=int(sys.argv[1])
        if sys.argv[2] != " ":
            ending_line=int(sys.argv[2]) 
    elif len(sys.argv) >= 2:
        if sys.argv[1] != " ":
            starting_line=int(sys.argv[1])        
    #print(sys.argv[1])
    #print(sys.argv[2])
            
    
    print("starting_line:",starting_line)
    print("ending_line:",ending_line)
    
    #count=starting_line
    
    print("count:",count)

    if file_name != "":
        with open(file_name) as MYFILE:
            for line in MYFILE:
                #print(line)
                each_line=line
                count += 1
                if starting_line <= count <= ending_line:
                    print(each_line,end="~")
                    
                    
def main():
    inspector()           
    
    
if __name__ == '__main__':
    main()                     