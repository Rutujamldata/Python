# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 16:40:38 2023

@author: rutuja
"""

'''This module implements a number of iterator building blocks inspired by constructs from APL, 
Haskell, and SML." In simple words, the number of iterators can together create 'iterator algebra' 
which makes it possible to complete the complex task. The functions in itertools are used to 
produce more complex iterators. Let's take an example: Python built-in zip() function accepts 
any number of arguments as iterable. It iterates over tuples and return their corresponding elements.'''

a = [1,2,3]  
b= ['a', 'b', 'c']  
c = zip(a,b)  
print(c) 

a = iter('Hello')  
print(a)  

'''Types of Iterator
There are various types of iterator in itertools module. The list is given below:
Infinite iterators
Combinatoric iterators
Terminating iterators'''


'''count(start, stop): 
It prints from the start value to infinite. The step argument is optional, 
if the value is provided to the step then the number of steps will be skipped.'''
import itertools  
  
for i in itertools.count(10,5):  
    if i == 50:  
        break  
    else:  
        print(i,end=" ")  
        


'''cycle(iterable): 
This iterator prints all value in sequence from the passed argument.
It prints the values in a cyclic manner.'''

import itertools  
temp = 0  
for i in itertools.cycle("123"):  
    if temp > 7:  
        break  
    else:  
        print(i,end=' ')  
        temp = temp+1          
        
        
import itertools  
  
val = ['Java', 'T', 'Point']  
  
iter = itertools.cycle(val)  
  
for i in range(6):  
    # Using next function  
    print(next(iter), end = " ")          
    
    
    
'''repeat(val,num): 
As the name suggests, it repeatedly prints the passed value for infinite time. 
The num argument is optional. '''    
    
import itertools  
print("Printing the number repeadtly:")  
print(list(itertools.repeat(40,15)))      



'''Combinatoric iterators: 
The complex combinatorial constructs are simplified by the recursive generators. 
The permutations, combinations, and Cartesian products are the example of the combinatoric construct.'''

from itertools import product  
  
print("We are computing cartesian product using repeat Keyword Argument:")  
print(list(product([1, 2], repeat=2)))  
print()  
  
print("We are computing cartesian product of the containers:")  
print(list(product(['Java', 'T', 'point'], '5')))  
print()  
  
print("We are computing product of the containers:")  
print(list(product('CD', [4, 5])))  





'''Permutations(): 
    It is used to generate all possible permutation of an iterable. 
    The uniqueness of each element depends upon their position instead of values. 
    It accepts two argument iterable and group_size. If the value of group_size is 
    none or not specified then group_size turns into length of the iterable.'''
from itertools import permutations  
  
print("Computing all permutation of the following list")  
print(list(permutations([3,"Python"],2)))  
print()  
  
print("Permutations of following string")  
print(list(permutations('AB')))  
print()  
  
print("Permutation of the given container is:")  
print(list(permutations(range(4),2)))



'''Combinations(): It is used to print all the possible combinations (without replacement) 
of the container which is passed as argument in the specified group size in sorted order.'''


from itertools import combinations  
print("Combination of list in sorted order(without replacement)",list(combinations(['B',3],2)))  
print()  
  
print("Combination of string in sorted order",list(combinations("ZX",2)))  
print()  
  
print("Combination of list in sorted order",list(combinations(range(20),1)))  





'''Combination_with_replacement(): 
    It accepts two arguments, first argument is a r-length tuple and 
    the second argument is repetition. It returns a subsequence of length n 
    from the elements of the iterable and repeat the same process. 
    Separate elements may repeat itself in combination_with_replacement()'''
    
    
from itertools import combinations_with_replacement  
  
print("Combination of string in sorted order(with replacement) is:")  
print(list(combinations_with_replacement("XY", 3)))  
print()  
  
print("Combination of list in sorted order(with replacement) is:")  
print(list(combinations_with_replacement([4, 2], 3)))  
print()  
  
print("Combination of container in sorted order(with replacement) is:")  
print(list(combinations_with_replacement(range(3), 2)))  



'''Terminating Iterator
Terminating iterators are generally used to work on the small input sequence and 
generate the output based on the functionality of the method used in iterator.'''

'''accumulate(iter, func): 
It takes two arguments, the first argument is iterable and the second is a 
function which would be followed at each iteration of value in iterable. If the 
function is not defined in accumulate() iterator, addition takes place by default. 
The output iterable depends on the input iterable; if input iterable contains no 
value then the output iterable will also be empty.'''



import itertools  
import operator  
  
# initializing list 1  
list1 = [1, 4, 5, 7, 9, 11]  
  
# using accumulate() that will prints the successive summation of elements  
print("The sum is : ", end="")  
print(list(itertools.accumulate(list1)))  
  
# using accumulate() that will prints the successive multiplication of elements  
print("The product is : ", end="")  
print(list(itertools.accumulate(list1, operator.mul)))  
  
  
# using accumulate() that will prints the successive summation of elements  
print("The sum is : ", end="")  
print(list(itertools.accumulate(list1)))  
  
# using accumulate() that will prints the successive multiplication of elements  
print("The product is : ", end="")  
print(list(itertools.accumulate(list1, operator.mul)))  


'''chain(iter1, iter2) - 
It is used to print all the values in iterable passed in the form of chain and declared in arguments.'''

import itertools  
  
# declaring list 1  
list1 = [1, 2, 3, 4]  
  
# declaring list 2  
list2 = [1, 5, 6, 8]  
  
# declaring list 3  
list3 = [9, 10, 11, 12]  
  
# using chain() function that will to print all elements of lists  
print("The output is : ", end="")  
print(list(itertools.chain(list1, list2, list3)))  


'''dropwhile(func, seq) - 
It starts printing the character only after the func.'''

import itertools  
# initializing list  
list1 = [2, 4, 5, 7, 8]  
# using dropwhile() iterator that will print start displaying after condition is false  
print("The output is : ", end="")  
print(list(itertools.dropwhile(lambda x: x % 2 == 0, list1)))  


'''filterfalse(func,seq) - 
We can assume it by its name, as this iterator prints only those values that return false 
for the passed function. '''

import itertools  
  
# declaring list  
list1 = [12, 14, 15, 27, 28]  
  
# using filterfalse() iterator that will print false values  
print("The Output is: ", end="")  
print(list(itertools.filterfalse(lambda x: x % 2 == 0, list1)))  


'''islice(iterable,start,stop,step) - 
It slices the given iterable according to given position. 
It accepts four arguments respectively and these are iterable, container, starting pos., 
ending position and step(optional)'''

import itertools  
# Declaring list  
list1 = [12, 34, 65, 73, 80, 19, 20]  
# using islice() iterator that will slice the list acc. to given argument  
# starts printing from 3nd index till 8th skipping 2  
print("The sliced list values are : ", end="")  
print(list(itertools.islice(list1, 2, 8, 2)))  


'''starmap(func, tuple list) - 
It takes two arguments; first argument is function and second argument is list which 
consists element in the form of tuple.'''

import itertools  
  
# Declaring list that contain tuple as element  
list1 = [(10, 20, 15), (18, 40, 19), (53, 42, 90), (16, 12, 27)]  
  
# using starmap() iterator for selection value acc. to function  
# selects max of all tuple values  
print("The values acc. to function are : ", end="")  
print(list(itertools.starmap(max, list1)))  


'''takewhile(func, iterable) - 
It is visa-versa of dropwhile(). It will print values until it returns false condition.'''
import itertools  
  
# Defining a list  
list1 = [20, 42, 64, 77, 8, 10, 20]  
  
# takewhile() iterator is used  to print values till condition return false.  
print("Print until 1st false value returned : ", end="")  
print(list(itertools.takewhile(lambda x: x % 2 == 0, list1)))  


'''tee(iterator, count) - 
It divides the container into a number of iterators which is defined in the argument. '''
# Declaring list  
li = [1, 2, 3, 4, 5, 6, 7]  
  
# storing list in iterator  
iti = iter(li)  
# using tee() iterator to create a list of iterators  
# Creating list of 3 iterators having similar values.  
it = itertools.tee(iti, 3)  
# It will print object of iterator  
print(it)  
print("The iterators are : ")  
for i in range(0, 2):  
    print(list(it[i]))  


'''zip_longest(iterable1, iterable2, fillval) - 
It prints the values of iterable alternatively in sequence. 
If one of the iterable prints all values, remaining values are 
filled by the values assigned to fill value.'''

import itertools  
print(" The combined value of iterrables is :")  
print(*(itertools.zip_longest('Java', 'Tpoint', fillvalue='_'))) 
