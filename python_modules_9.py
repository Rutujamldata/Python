# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 12:18:25 2023

@author: rutuja
"""

#Python Modules

import math  
print( "The value of euler's number is", math.e )  

import math as mt  
print( "The value of euler's number is", mt.e )  

from math import e  
print( "The value of euler's number is", e )  

# Python program to show how to import multiple objects from a module  
from math import e, tau  
print( "The value of tau constant is: ", tau )  
print( "The value of the euler's number is: ", e )  

# importing the complete math module using *  
from math import *  
    
# accessing functions of math module without using the dot operator  
print( "Calculating square root: ", sqrt(25) )  
print( "Calculating tangent of an angle: ", tan(pi/6) ) # here pi is also imported from the math module  

# We will import the sys module  
import sys  
print(sys.path) 


# Dir-built in Function
# Python program to print the directory of a module  
print( "List of functions:\n ", dir( str ), end=", " )  
