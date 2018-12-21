# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 12:06:36 2018

@author: calydon
"""

def print_line(FH):
    with open(FH) as MYFILE:
        for line in MYFILE:
            print(line,end="")
            
def main():
    File_name='alpha.txt'
    print_line(File_name)            
    
    
if __name__ == '__main__':
    main()    