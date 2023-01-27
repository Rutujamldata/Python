# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 12:44:50 2023

@author: rutuja
"""

#In Python, the for loop is used to run a block of code for a certain number of times. 
#It is used to iterate over any sequences such as list, tuple, string, etc.

#syntax
# for val in sequence:
#     # statement(s)
'''In programming, loops are used to repeat a block of code. For example, if we want to show a message 100 times, then we can use a loop.''' 

#Loop over python list
languages = ['Swift', 'Python', 'Go', 'JavaScript']

# access items of a list using for loop
for language in languages:
    print(language)
    
    
#Python for Loop with Python range()
#A range is a series of values between two numeric intervals.
#We use Python's built-in function range() to define a range of values. 
values = range(4)

# use of range() to define a range of values
values = range(4)

# iterate from i = 0 to i = 3
for i in values:
    print(i)
    
#Here we get the value from 0 to 3 because we use for loop and get all the value 


#Python for loop with else
#A for loop can have an optional else block as well. 
#The else part is executed when the loop is finished.digits = [0, 1, 5]
digits = [0, 1, 5]
for i in digits:
    print(i)
else:
    print("No items left.")   
    
    
    
# While Loop
#Python while loop is used to run a block code until a certain condition is met.
#The syntax of while loop is:    
# while condition:
#     # body of while loop


'''A while loop evaluates the condition
If the condition evaluates to True, the code inside the while loop is executed.
condition is evaluated again.
This process continues until the condition is False.
When condition evaluates to False, the loop stops.'''

# program to display numbers from 1 to 5

# initialize the variable
i = 1
n = 5

# while loop from i = 1 to 5
while i <= n:
    print(i)
    i = i + 1
    

# program to calculate the sum of numbers
# until the user enters zero

total = 0

number = int(input('Enter a number: '))

# add numbers until number is zero
while number != 0:
    total += number    # total = total + number
    
    # take integer input again
    number = int(input('Enter a number: '))
    

print('total =', total)

#In the above example, the while iterates until the user enters zero. When the user enters zero, 
#the test condition evaluates to False and the loop ends.


'''Infinite while loop'''
age = 32
# the test condition is always True
while age > 18:
    print('You can vote')

#In the above example, the condition always evaluates to True. Hence, the loop body will run for infinite times.


'''Python While loop with else'''
#In Python, a while loop may have an optional else block.
#Here, the else part is executed after the condition of the loop evaluates to False.
counter = 0

while counter < 3:
    print('Inside loop')
    counter = counter + 1
else:
    print('Inside else')
    
'''The break is a keyword in python which is used to bring the program control out of the loop. 
The break statement breaks the loops one by one, i.e., in the case of nested loops, 
it breaks the inner loop first and then proceeds to outer loops. In other words, 
we can say that break is used to abort the current execution of the program and the control goes to the next line after the loop.'''
#break statement
counter = 0

while counter < 3:
    # loop ends because of break
    # the else part is not executed 
    if counter == 1:
        break

    print('Inside loop')
    counter = counter + 1
else:
    print('Inside else')    
    
# second example
list =[1,2,3,4]  
count = 1;  
for i in list:  
    if i == 4:  
        print("item matched")  
        count = count + 1 
        break  
print("found at",count,"location")


# Example
str = "python"  
for i in str:  
    if i == 'o':
        break  
    print(i)

#Break statement with while loop
i = 0
while 1:  
    print(i," ",end="") 
    i=i+1
    if i == 10:  
        break  
print("came out of while loop") 


#Printing tables serially
n=2  
while 1:  
    i=1;  
    while i<=10:  
        print("%d X %d = %d\n"%(n,i,n*i))
        i = i+1;  
    choice = int(input("Do you want to continue printing the table, press 0 for no?"))  
    if choice == 0:  
        break    
    n=n+1  
    
    
'''Python Continue Statement'''
#In Python, loops repeat processes on their own in an efficient way. 
#However, there might be occasions when we wish to leave the current loop entirely, skip iteration, or 
#dismiss the condition controlling the loop. We use Loop control statements in such cases. 
#The continue keyword is a loop control statement that allows us to change the loop's control.     

'''Python code to show example of continue statement ''' 
   
# looping from 10 to 20  
for iterator in range(10, 21):  
   
    # If iterator is equals to 15, loop will continue to the next iteration  
    if iterator == 15:  
        continue  
    # otherwise printing the value of iterator  
    print( iterator )     


#Exammple
# Creating a string  
string = "JavaTpoint"  
# initializing an iterator  
iterator = 0  
   
# starting a while loop                   
while iterator < len(string):  
    # if loop is at letter a it will skip the remaining code and go to next iteration  
    if string[iterator] == 'a':    
        continue    
    # otherwise it will print the letter  
    print(string[ iterator ])  
    iterator += 1  


string = "Ajay"  
# initializing an iterator  
iterator = 0  
   
# starting a while loop                   
while iterator < len(string):  
    # if loop is at letter a it will skip the remaining code and go to next iteration  
    if string[iterator] == 'a':    
        continue    
    # otherwise it will print the letter  
    print(string[ iterator ])  
    iterator += 1  


string = "Ajay"  
# initializing an iterator  
iterator = 0  
   
# starting a while loop                   
while iterator < len(string):  
    # if loop is at letter a it will skip the remaining code and go to next iteration  
    if string[iterator] == 'A':    
        continue    
    # otherwise it will print the letter  
    print(string[ iterator ])  
    iterator += 1  



# Continue vs Pass statement
'''
Continue - The continue statement is utilized to skip the current loop's remaining statements, 
           go to the following iteration,and return control to the beginning.
           It takes the control back to the start of the loop.
           It works with both the Python while and Python for loops.
           
Pass - The pass keyword is used when a phrase is necessary syntactically to be placed but not to be executed.           
       Nothing happens if the Python interpreter encounters the pass statement.
       It performs nothing; hence it is a null operation.'''
       
# Pass Statement
#The null statement is another name for the pass statement. 
#A Comment is not ignored by the Python interpreter, whereas a pass statement is not. 
#Hence, they two are different Python keywords.      

# Python program to show how to use a pass statement in a for loop  
'''''pass acts as a placeholder. We can fill this place later on'''  
sequence = {"Python", "Pass", "Statement", "Placeholder"}  
for value in sequence:  
    if value == "Pass":  
        pass # leaving an empty if block using the pass keyword  
    else:  
        print("Not reached pass keyword: ", value)   


# Python program to show how to create an empty function and an empty class  
  
# Empty function:  
def empty():  
    pass  
  
# Empty class  
class Empty:  
    pass  
