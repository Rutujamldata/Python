# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 11:44:25 2023

@author: rutuja
"""


'''Generator functions allow you to declare a function that behaves 
like an iterator.'''


'''Generator-Function: A generator-function is defined like a normal function,
but whenever it needs to generate a value, it does so with the yield keyword 
rather than return. 
If the body of a def contains yield, the function automatically becomes 
a generator function.'''


'''The yield statement suspends a function’s execution and sends 
a value back to the caller, but retains enough state to enable the 
function to resume where it left off. When the function resumes, 
it continues execution immediately after the last yield run. 
This allows its code to produce a series of values over time, 
rather than computing them at once and sending them back like a list.'''


def simple():  
 for i in range(10):  
    if(i%2==0):  
         yield i  
  
#Successive Function call using for loop  
for i in simple():  
    print(i)  
    
    
# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
    yield 1           
    yield 2           
    yield 3           
  
# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)  
    
    
    
# A Python program to demonstrate use of
# generator object with next()
 
# A generator function
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
  
# x is a generator object
x = simpleGeneratorFun()
 
# Iterating over the generator object using next
print(next(x)) # In Python 3, __next__()
print(next(x))
print(next(x))    
    
    
    
'''A simple generator for Fibonacci Numbers'''
def fib(limit):
     
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1
 
    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b
 
# Create a generator object
x = fib(5)
 
# Iterating over the generator object using next
print(next(x)) # In Python 3, __next__()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
 
# Iterating over the generator object using for
# in loop.
print("\nUsing for in loop")
for i in fib(5):
    print(i)
    
    
    
'''Suppose we create a stream of Fibonacci numbers, 
adopting the generator approach makes it trivial; we just have to call 
next(x) to get the next Fibonacci number without bothering about where 
or when the stream of numbers ends. A more practical type of stream 
processing is handling large data files such as log files. Generators 
provide a space-efficient method for such data processing as only parts 
of the file are handled at one given point in time. 
We can also use Iterators for these purposes, but Generator provides 
a quick way (We don’t need to write __next__ and __iter__ methods here).''' 

a = range(5)
list(a)

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

for i in infinite_sequence():
     print(i, end=" ")
     
     
gen = infinite_sequence()
next(gen)     
next(gen)
next(gen)
next(gen)



def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return num
    else:
        return False
    
    
for i in infinite_sequence():
     pal = is_palindrome(i)
     if pal:
         print(i)    
         
         
         
# Using multiple yield statement
def multiple_yield():  
    str1 = "First String"  
    yield str1  
  
    str2 = "Second string"  
    yield str2  
  
    str3 = "Third String"  
    yield str3  
obj = multiple_yield()  
print(next(obj))  
print(next(obj))  
print(next(obj))         



'''Difference between Generator function and Normal function
Normal function contains only one Lreturn statement whereas generator 
function can contain one or more yield statement.
When the generator functions are called, the normal function is paused 
immediately and control transferred to the caller.
Local variable and their states are remembered between successive calls.
StopIteration exception is raised automatically when the function 
terminates.'''

#Generator expression

list = [1,2,3,4,5,6,7]  
  
# List Comprehension  
z = [x**3 for x in list]  
  
# Generator expression  
a = (x**3 for x in list)  
  
print(a)  
print(z)

'''In the above program, list comprehension has returned the list 
of cube of elements whereas generator expression has returned the 
reference of calculated value. Instead of applying a for loop, 
we can also call next() on the generator object. Let's consider 
another example:'''

list = [1,2,3,4,5,6]  
  
z = (x**3 for x in list)  
  
print(next(z))  
  
print(next(z))  
  
print(next(z))  
  
print(next(z))  


#Write a program to print the table of the given number using 
# the generator.

def table(n):  
    for i in range(1,11):  
        yield n*i  
        i = i+1  
  
for i in table(15):  
    print(i)  
    
    
    
'''Advantages of Generators
There are various advantages of Generators. 
Few of them are given below:

1. Easy to implement
Generators are easy to implement as compared to the iterator. 
In iterator, we have to implement __iter__() and __next__() function.

2. Memory efficient
Generators are memory efficient for a large number of sequences. 
The normal function returns a sequence of the list which creates 
an entire sequence in memory before returning the result, 
but the generator function calculates the value and pause 
their execution. It resumes for successive call. 
An infinite sequence generator is a great example of memory optimization.'''    




import sys  
# List comprehension  
nums_squared_list = [i * 2 for i in range(1000)]  
print(sys.getsizeof("Memory in Bytes:",nums_squared_list))  
# Generator Expression  
nums_squared_gc = (i ** 2 for i in range(1000))  
print(sys.getsizeof("Memory in Bytes:", nums_squared_gc))  

'''We can observe from the above output that list comprehension is using 
4508 bytes of memory, whereas generator expression is using 56 bytes 
of memory. It means that generator objects are much efficient than 
the list compression.'''
