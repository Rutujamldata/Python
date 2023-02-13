# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 11:57:29 2023

@author: user
"""


'''A Python list comprehension consists of brackets containing the expression, 
which is executed for each element along with the 
for loop to iterate over each element in the Python list. '''

#Syntax for list Comphrension
# newList = [ expression(element) for element in oldList if condition ] 

# Using list comprehension to iterate through loop
List = [character for character in [1, 2, 3]]
print(List)


#Even list using LC
list = [i for i in range(11) if i % 2 == 0]
print(list)


#matrix using LC
matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)


#List comprehension vs For loop
List = []
for character in 'Geeks 4 Geeks!':
    List.append(character)
print(List)

# Using list comprehension to iterate through loop
List = [character for character in 'Geeks 4 Geeks!']
print(List)



######################################################

# Import required module
import time
 
 
# define function to implement for loop
def for_loop(n):
    result = []
    for i in range(n):
        result.append(i**2)
    return result
 
 
# define function to implement list comprehension
def list_comprehension(n):
    return [i**2 for i in range(n)]
 
 
# Driver Code
 
# Calculate time taken by for_loop()
begin = time.time()
for_loop(10**6)
end = time.time()
 
# Display time taken by for_loop()
print('Time taken for_loop:', round(end-begin, 2))
 
# Calculate time takens by list_comprehension()
begin = time.time()
list_comprehension(10**6)
end = time.time()
 
# Display time taken by for_loop()
print('Time taken for list_comprehension:', round(end-begin, 2))


#############################################
#Nested List comprehension vs nested for loop
#For loop
matrix = []
for i in range(3):
 
    # Append an empty sublist inside the list
    matrix.append([])
 
    for j in range(5):
        matrix[i].append(j)
 
print(matrix)

# Nested list comprehension
matrix = [[j for j in range(5)] for i in range(3)]
 
print(matrix)



####################################################################
# Key Points
'''Comprehension of the list is an effective means of describing and constructing lists based on current lists.
Generally, list comprehension is more lightweight and simpler than standard list formation functions and loops.
We should not write long codes for list comprehensions in order to ensure user-friendly code.
Every comprehension of the list can be rewritten in for loop, but in the context of list interpretation, 
every for loop can not be rewritten.'''


########Python List Comprehension Using If-else#########
lis = ["Even number" if i % 2 == 0
       else "Odd number" for i in range(8)]
print(lis)

############Nested IF with List Comprehension#########

lis = [num for num in range(100)
       if num % 5 == 0 if num % 10 == 0]
print(lis)


########### Display square of numbers from 1 to 10.#########

# Getting square of number from 1 to 10
squares = [n**2 for n in range(1, 11)]
print(squares)

########Display Transpose of 2D- Matrix.##################
# Assign matrix
twoDMatrix = [[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]]
 
# Generate transpose
trans = [[i[j] for i in twoDMatrix] for j in range(len(twoDMatrix[0]))]
print(trans)



######### Toggle the case of each character in a string.############
# Initializing string
string = 'Geeks4Geeks'
# Toggle case of each character
List = list(map(lambda i: chr(ord(i) ^ 32), string))
# Display list
print(List)


#########Reverse each string in a tuple.################

# Reverse each string in tuple
List = [string[::-1] for string in ('Geeks', 'for', 'Geeks')]
print(List)


############Display the sum of digits of all the odd elements in a list.###########
# Explicit function
def digitSum(n):
    dsum = 0
    for ele in str(n):
        dsum += int(ele)
    return dsum
 
 
# Initializing list
List = [367, 111, 562, 945, 6726, 873]
newList = [digitSum(i) for i in List if i & 1]
print(newList)
