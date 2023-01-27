# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 16:45:38 2023

@author: rutuja
"""

'''A function is a collection of related assertions that performs a mathematical, analytical, or evaluative operation. 
A collection of statements called Python Functions returns the particular task. 
Python functions are simple to define and essential to intermediate-level programming. 
The exact criteria hold to function names as they do to variable names. 
The goal is to group up certain often performed actions and define a function. 
We may call the function and reuse the code contained within it with different variables rather than repeatedly 
creating the same code block for different input variables.

User-defined and built-in functions are the two main categories of functions in Python. 
It helps maintain the programme concise, unique, and well-structured.

Advantages of Functions in Python
Python functions have the following Perks.
By including functions, we can prevent repeating the same code block repeatedly in a program.
Python functions, once defined, can be called many times and from anywhere in a program.
If our Python program is large, it can be separated into numerous functions which is simple to track.
The key accomplishment of Python functions is we can return as many outputs as we want with different arguments.'''

# Syntax of python Function  
# def function_name( parameters ):  
#     # code block  

'''The beginning of a function header is indicated by a keyword called def.
function_name is the function's name that we can use to separate it from others. We will use this name to call the function later in the program. In Python, name functions must follow the same rules as naming variables.
We pass arguments to the defined function using parameters. However, they are optional.
The function header is terminated by a colon (:).
We can use a documentation string called docstring in the short form to explain the purpose of the function.
The body of the function is made up of several valid Python statements. The indentation depth of the whole code block must be the same (usually 4 spaces).
We can use a return expression to return a value from a defined function.'''

# Example Python Code for User-Defined function  
def square( num ):    
    """  
    This function computes the square of the number.  
    """    
    return num**2     
object_ = square(6)    
print( "The square of the given number is: ", object_ )    


'''Calling a Function
A function is defined by using the def keyword and giving it a name, specifying the arguments that must be passed to the function,
and structuring the code block.

After a function's fundamental framework is complete, we can call it from anywhere in the program. The following is an example 
of how to use the a_function function.'''

'''Pass by Reference vs. Pass by Value
All parameters in the Python programming language are provided by reference. 
It indicates that if we alter the value of an argument inside of a function, the calling function will likewise reflect the change.'''

# Example Python Code for Pass by Reference vs. Value  
# defining the function    
def square( item_list ):    
    '''''''This function will find the square of items in the list'''    
    squares = [ ]    
    for l in item_list:    
        squares.append( l**2 )    
    return squares    
    
# calling the defined function    
my_list = [17, 52, 8];    
my_result = square( my_list )    
print( "Squares of the list are: ", my_result )     

#Function Arguments
'''
Default arguments
Keyword arguments
Required arguments
Variable-length arguments'''


'''1) Default Arguments'''
# A default argument is a kind of parameter that takes as input a default value if no value is 
# supplied for the argument when the function is called. Default arguments are demonstrated in the following instance.
# Python code to demonstrate the use of default arguments    
# defining a function    
def function( n1, n2 = 20 ):    
    print("number 1 is: ", n1)    
    print("number 2 is: ", n2)    
     
     
# Calling the function and passing only one argument    
print( "Passing only one argument" )    
function(30)    
    
# Now giving two arguments to the function    
print( "Passing two arguments" )    
function(50,30)    

'''2) Keyword Arguments'''
# A function called's arguments are linked to keyword arguments. When invoking a function with keyword arguments, 
# the user may tell whose parameter value it is by looking at the parameter label.

# We can remove certain arguments or arrange them in a different order since the Python interpreter will connect the 
# provided keywords to link the values with its parameters. Another way to use keywords to invoke the function() method is as follows:
    
# Python code to demonstrate the use of keyword arguments    
  # Defining a function    
def function( n1, n2 ):    
    print("number 1 is: ", n1)    
    print("number 2 is: ", n2)    
    
# Calling function and passing arguments without using keyword    
print( "Without using keyword" )    
function( 50, 30)       
        
# Calling function and passing arguments using keyword    
print( "With using keyword" )    
function( n2 = 50, n1 = 30)    

'''3)Required Arguments'''
# The arguments given to a function while calling in a pre-defined positional sequence are required arguments.
# The count of required arguments in the method call must be equal to the count of arguments provided while defining the function.

# We must send two arguments to the function function() in the correct order, or it will return a syntax error, as seen below.

# Python code to demonstrate the use of default arguments      
# Defining a function    
def function( n1, n2 ):    
    print("number 1 is: ", n1)    
    print("number 2 is: ", n2)    
    
# Calling function and passing two arguments out of order, we need num1 to be 20 and num2 to be 30    
print( "Passing out of order arguments" )    
function( 30, 20 )       
    
# Calling function and passing only one argument    
print( "Passing only one argument" )    
try:    
    function( 30 )    
except:    
    print( "Function needs two positional arguments" )  




'''4) Variable-Length Arguments'''
# We can use special characters in Python functions to pass as many arguments as we want in a function. 
# There are two types of characters that we can use for this purpose:

# *args -These are Non-Keyword Arguments
# **kwargs -These are Keyword Arguments.


# Python code to demonstrate the use of variable-length arguments       
# Defining a function    
def function( *args_list ):    
    ans = []    
    for l in args_list:    
        ans.append( l.upper() )    
    return ans    
# Passing args arguments    
object = function('Python', 'Functions', 'tutorial')    
print( object )    
    
'''Defining a function'''    
def function( **kargs_list ):    
    ans = []    
    for key, value in kargs_list.items():    
        ans.append([key, value])    
    return ans    
# Paasing kwargs arguments    
object = function(First = "Python", Second = "Functions", Third = "Tutorial")    
print(object) 




'''Return Statement'''
# We write a return statement in a function to leave a function and give the calculated value when a 
# defined function is called.

# Python code to demonstrate the use of return statements      
# Defining a function with return statement    
def square( num ):    
    return num**2    
     
# Calling function and passing arguments.    
print( "With return statement" )    
print( square( 52 ) )    
    
# Defining a function without return statement     
def square( num ):    
     num**2     
    
# Calling function and passing arguments.    
print( "Without return statement" )    
print( square( 52 ) )    

'''The Anonymous Functions/ Lambda Function'''
# These types of Python functions are anonymous since we do not declare them, as we declare usual functions, 
# using the def keyword. We can use the lambda keyword to define the short, single output, anonymous functions.

# Lambda expressions can accept an unlimited number of arguments; however, they only return one value as 
# the result of the function. They can't have numerous expressions or instructions in them. 
# Since lambda needs an expression, an anonymous function cannot be directly called to print.

# Lambda functions contain their unique local domain, meaning they can only reference variables in 
# their argument list and the global domain name.

# Python code to demonstrate ananymous functions  
# Defining a function    
lambda_ = lambda argument1, argument2: argument1 + argument2;    
    
# Calling the function and passing values    
print( "Value of the function is : ", lambda_( 20, 30 ) )    
print( "Value of the function is : ", lambda_( 40, 50 ) )    

'''Python Function within Another Function'''
# Functions are considered first-class objects in Python. In a programming language, 
# first-class objects are treated the same wherever they are used. They can be used in conditional expressions, 
# as arguments, and saved in built-in data structures. A programming language is considered to implement 
# first-class functions if it treats functions as first-class objects. The concept of First Class functions 
# is supported by Python.

# Inner or nested function refers to a function defined within another defined function. 
# Inner functions can access the parameters of the outer scope. Inner functions are constructed to cover them 
# from the changes that happen outside the function. Many developers regard this process as encapsulation.

def word():    
    string = 'Python functions tutorial'    
    x = 5     
    def number():    
        print( string )   
        print( x )  
             
    number()    
word() 
