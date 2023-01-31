# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 11:44:24 2023

@author: rutuja
"""

# Python Lambda Functions

'''Syntax of Python Lambda Function
lambda arguments: expression'''

#Example
#An example of a lambda function that adds 4 to the input number
add = lambda num: num + 4  
print( add(6) )  


#Comparison of normal def function
def add( num ):  
   return num + 4  
print( add(6) )  


#Another example for comparision
# Python code to show the reciprocal of the given number to highlight the difference between def() and lambda().  
def reciprocal( num ):  
    return 1 / num  
   
lambda_reciprocal = lambda num: 1 / num  
   
# using the function defined by def keyword  
print( "Def keyword: ", reciprocal(6) )  
   
# using the function defined by lambda keyword  
print( "Lambda keyword: ", lambda_reciprocal(6) )  


'''Using Lambda Function with filter()'''
# Code to filter odd numbers from a given list  
list_ = [34, 12, 64, 55, 75, 13, 63]  
odd_list = list(filter( lambda num: (num % 2 != 0) , list_ ))  
print(odd_list)  



'''Using Lambda Function with map()'''
#Code to calculate the square of each number of a list using the map() function  
numbers_list = [2, 4, 5, 1, 3, 7, 8, 9, 10]    
squared_list = list(map( lambda num: num ** 2 , numbers_list ))  
print( squared_list )  


'''Using Lambda Function with if-else'''
# Code to use lambda function with if-else  
Minimum = lambda x, y : x if (x < y) else y  
print(Minimum( 35, 74 ))  


'''Using Lambda with Multiple Statements'''
# Code to print the third-largest number of the given list using the lambda function  
my_List = [ [3, 5, 8, 6], [23, 54, 12, 87], [1, 2, 4, 12, 5] ]  
# sorting every sublist of the above list  
sort_List = lambda num : ( sorted(n) for n in num )  
# Getting the third largest number of the sublist  
third_Largest = lambda num, func : [ l[ len(l) - 2] for l in func(num)]  
result = third_Largest( my_List, sort_List)  
print( result ) 


'''Using Lambda Function with List Comprehension'''
#Code to calculate square of each number of list using list comprehension  
squares = [lambda num = num: num ** 2 for num in range(0, 11)]  
for square in squares:  
    print( square(), end = " ")  




