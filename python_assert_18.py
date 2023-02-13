# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 11:51:50 2023

@author: rutuja
"""

#Assertion
'''
It is a debugging tool, and its primary task is to check the condition. 
If it finds that the condition is true, 
it moves to the next line of code, and If not, 
then stops all its operations and throws an error. 
It points out the error in the code.'''


#Syntax - assert condition, error_message(optional)    

#Where Assertion in Python used
'''
Checking the outputs of the functions.
Used for testing the code.
In checking the values of arguments.Checking the valid input.'''

def avg(scores):    
    assert len(scores) != 0,"The List is empty."    
    return sum(scores)/len(scores)    
    

scores2 = [67,59,86,75,92]    
print("The Average of scores2:",avg(scores2))    
    
scores1 = []    
print("The Average of scores1:",avg(scores1))    


# initializing number     
x = 7    
y = 0    
# It uses assert to check for 0     
print ("x / y value is : ")     
assert y != 0, "Divide by 0 error"    
print (x / y)  


