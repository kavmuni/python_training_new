# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 11:25:17 2018

@author: calydon
"""

def captain_names():
    names_matched=set()
    names_dict=dict()
    #names_dict_ordered=dict()
    names_match_list=list()
    FH="captains.txt"
    with open(FH) as MYFILE:
        for line in MYFILE:
            each_line=line.split(',')
            #print(each_line)
            if each_line[0] != 'Player':
                names_matched=(each_line[0],int(each_line[2]))
                #print(names_matched)
                names_match_list.append(names_matched)
                #names_dict[each_line[0]]=each_line[2]
    
    names_match_list.sort()
    #print(names_match_list)
    for item in names_match_list:
        names_dict[item[0]]=item[1]
        #print(item[0])
    #sorted(names_dict)        
    print(names_dict)
    
    #for item in sorted(names_dict, key=names_dict.get):
        #print (item, names_dict[item])
        #names_dict_ordered[item]=names_dict[item]
    #print(names_dict_ordered.values())
    print("-------------------------------")        
    print("Maximum number of matches were played by",max(names_dict, key=names_dict.get))
    print("-------------------------------")            
    with open(FH) as MYFILE:
        header=next(MYFILE)
        for line in MYFILE:
            each_line=line.split(',')
            names_dict[each_line[0]]=[int(each_line[2]),int(each_line[3])]
    print(names_dict)     
    print("-------------------------------")        
    print("Maximum number of matches were played by",max(names_dict, key=names_dict.get))
                
def main():
    captain_names()           
    
    
if __name__ == '__main__':
    main()              