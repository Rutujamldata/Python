# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 11:33:54 2023

@author: rutuja
"""

'''Python Decoraters'''
# In Decorators, functions are passed as an argument into another function 
# and then called inside the wrapper function.

# Python program to illustrate functions
# can be treated as objects
def shout(text):
    return text.lower()
 
print(shout('Hello'))
 
yell = shout
 
print(yell('Hello'))



'''Passing the function as argument'''
# Python program to illustrate functions
# can be passed as arguments to other functions
def shout(text):
    return text.upper()
 
def whisper(text):
    return text.lower()
 
def greet(func):
    # storing the function in a variable
    greeting = func("""Hi, I am created by a function passed as an argument.""")
    print (greeting)
 
greet(shout)
greet(whisper)
