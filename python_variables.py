# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 11:02:59 2023

@author: rutuja
"""
'''
Variable is a name that is used to refer to memory location. Python variable is also known as an identifier and used to hold value.
Identifier Naming
Variables are the example of identifiers. An Identifier is used to identify the literals used in the program. 
The rules to name an identifier are given below.
The first character of the variable must be an alphabet or underscore ( _ ).
All the characters except the first character may be an alphabet of lower-case(a-z), upper-case (A-Z), underscore, or digit (0-9).
Identifier name must not contain any white-space, or special character (!, @, #, %, ^, &, *).
Identifier name must not be similar to any keyword defined in the language.
Identifier names are case sensitive; for example, my name, and MyName is not the same.
Examples of valid identifiers: a123, _n, n_9, etc.
Examples of invalid identifiers: 1a, n%4, n 9, etc.
'''
#Variable assignment
a = 'Rutuja'
b = 10
c = 'c'
l = 28.34


#valib variables naming

name = "A"  
Name = "B"  
naMe = "C"  
NAME = "D"  
n_a_m_e = "E"  
_name = "F"  
name_ = "G"  
_name_ = "H"  
na56me = "I"  
  
'''Camel Case - In the camel case, each word or abbreviation in the middle of begins with a capital letter. 
There is no intervention of whitespace. For example - nameOfStudent, valueOfVaraible, etc.
Pascal Case - It is the same as the Camel Case, but here the first word is also capital. For example - NameOfStudent, etc.
Snake Case - In the snake case, Words are separated by the underscore. For example - name_of_student, etc.
'''

#object reference
a = 50
b = a

#object identity
a1 = id(a)
b1 = id(b)
#here is the same id for a1 and b1 because on the line 47 & 48 with did object refrence so a and b point to single value is 50
print(a1,b1)


#MULTIPLE ASSIGNMENT
#Assigning single value to multiple variables
x=y=z=50    
print(x,y,z)

#Assigning multiple values to multiple variables
x,y,z = 10,20,30


#variables Types
#Local variables 
#Local variables are the variables that declared inside the function and have scope within the function.
# Declaring a function  
def add():  
    # Defining local variables. They has scope only within a function  
    x1 = 20  
    x2 = 30  
    c1 = x1 + x2  
    print("The sum is:", c1)  
  
# Calling a function  
add()  
print (x1)
'''print (x1)
Traceback (most recent call last):

  Cell In[26], line 1
    print (x1)

NameError: name 'x1' is not defined'''

#Gloabal Variables
# Declare a variable and initialize it  
x11 = 101  
  
# Global variable in function  
def mainFunction():  
    # printing a global variable  
    global x11  
    print(x11)  
    # modifying a global variable  
    x = 'Welcome To Javatpoint'  
    print(x11)  
  
mainFunction()  
print(x11)  

#Delete Variables
del x11



