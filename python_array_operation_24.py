# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 12:40:17 2023

@author: rutuja
"""

'''
Array operations
Some of the basic operations supported by an array are as follows:
Traverse - It prints all the elements one by one.
Insertion - It adds an element at the given index.
Deletion - It deletes an element at the given index.
Search - It searches an element using the given index or by the value.
Update - It updates an element at the given index.'''


from array import *  
arrayName = array(typecode, [initializers])   

import array as arr  
a = arr.array('i', [2, 4, 6, 8])  
print("First element:", a[0])  
print("Second element:", a[1])  
print("Second last element:", a[-1]) 

# how to change or add elements
import array as arr  
numbers = arr.array('i', [1, 2, 3, 5, 7, 10])  
   
# changing first element  
numbers[0] = 0     
print(numbers)    # Output: array('i', [0, 2, 3, 5, 7, 10])  
   
# changing 3rd to 5th element  
numbers[2:5] = arr.array('i', [4, 6, 8])    
print(numbers)    # Output: array('i', [0, 2, 4, 6, 8, 10])  


#Delete the array element
import array as arr  
number = arr.array('i', [1, 2, 3, 3, 4])  
del number[2]                           # removing third element  
print(number)                           # Output: array('i', [1, 2, 3, 4])  


#Finding the length of the array
len(number)

#Array Concatenations
a=arr.array('d',[1.1 , 2.1 ,3.1,2.6,7.8])  
b=arr.array('d',[3.7,8.6])  
c=arr.array('d')  
c=a+b  
print("Array c = ",c)  

import array as arr  
x = arr.array('i', [4, 7, 19, 22])  
print("First element:", x[0])  
print("Second element:", x[1])  
print("Second last element:", x[-1])  
