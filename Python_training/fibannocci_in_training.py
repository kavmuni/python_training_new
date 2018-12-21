# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:08:50 2018

@author: calydon
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 19:47:10 2018

@author: Muniappan
"""

def fibannoci(start_num=0,end_num=10000,n_count=10,for_even=0,min_num=0):
    num_01=start_num
    num_02=start_num + 1
    count=0
    #print("starting")
    if n_count < 0:
        print("Please enter a positive count")
    elif n_count == 1:
        print("The series is :",num_01)
    else:
        print("The series is :")
        while count < n_count and num_01 < end_num:
            even_num = num_01 % 2
            if for_even==1 and even_num == 0 and num_01 >= min_num:
                print(num_01,end=' , ')
                count -= 2
            elif for_even==0:
                print(num_01,end=' , ')
            temp=num_01 + num_02
            num_01 = num_02
            num_02 = temp
            count += 1
    print("\n")               
                         
            
def main():
    fibannoci(start_num=0,n_count=10)#first 10 fibannocci numbers            
    fibannoci(start_num=0,n_count=20)#first 20 fibannocci numbers
    fibannoci(start_num=0,n_count=9)#first 9 fibannocci numbers
    fibannoci(start_num=0,end_num=1000000,n_count=10,for_even=1)#first 10 even fibannocci numbers
    fibannoci(start_num=0,end_num=1000,for_even=1,min_num=100,n_count=1000)#all even 3 digit fibannocci numbers
    
main()    