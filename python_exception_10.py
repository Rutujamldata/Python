# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 12:25:36 2023

@author: rutuja
"""

#Python Exception
'''Try and except statements are used to catch and handle exceptions in Python. 
Statements that can raise exceptions are kept inside the try clause and 
the statements that handle the exception are written inside except clause.'''

# # Python code to catch an exception and handle it using try and except code blocks  
   
a = ["Python", "Exceptions", "try and except"]  
try:  
    #looping through the elements of the array a, choosing a range that goes beyond the length of the array  
     for i in range( 4 ):  
        print( "The index and element from the array is", i, a[i] )  
#if an error occurs in the try block, then except block will be executed by the Python interpreter       
except:  
    print ("Index out of range")  
    
    
#How to Raise an Exception
#Python code to show how to raise an exception in Python  
num = [3, 4, 5, 7]  
if len(num) > 3:  
    raise Exception( f"Length of the given list must be less than or equal to 3 but is {len(num)}" )


#Python Assertion
'''Programmers often place assertions at the start of a function to check for valid input, 
and after a function call to check for valid output. When it encounters an assert statement, 
Python evaluates the accompanying expression, which is hopefully true. 
If the expression is false, Python raises an AssertionError exception.'''

#Python program to show how to use assert keyword  
# defining a function  
def square_root( Number ):  
    assert ( Number < 0), "Give a positive integer"  
    return Number**(1/2)  
  
#Calling function and passing the values  
print( square_root( 36) )  
print( square_root( -36 ) )     



'''Try with Else Clause'''
# Python also supports the else clause, which should come after every except clause,
# in the try, and except blocks. Only when the try clause fails to throw an 
# exception the Python interpreter goes on to the else block.   

# Python program to show how to use else clause with try and except clauses  
  
# Defining a function which returns reciprocal of a number  
def reciprocal( num1 ):  
    try:  
        reci = 1 / num1  
    except ZeroDivisionError:  
        print( "We cannot divide by zero" )  
    else:  
        print ( reci )  
# Calling the function and passing values  
reciprocal( 4 )  
reciprocal( 0 )  


'''Finally Keyword in Python'''
# The finally keyword is available in Python, and it is always used after the try-except block. 
# The finally code block is always executed after the try block has terminated normally or after 
# the try block has terminated for some other reason.
# Python code to show the use of finally clause  
# Raising an exception in try block  
try:  
    div = 4 // 0    
    print( div )  
# this block will handle the exception raised  
except ZeroDivisionError:  
    print( "Atepting to divide by zero" )  
# this will always be executed no matter exception is raised or not  
finally:  
    print( 'This is code of finally clause' )  
