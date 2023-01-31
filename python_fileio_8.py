# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 12:10:10 2023

@author: rutuja
"""

# Python File Handling

# The file handling plays an important role when the data needs to be stored permanently into the file. 
# A file is a named location on disk to store related information. 
# We can access the stored information (non-volatile) after the program termination

#File Operations
# 1)Open a file
# 2)Read or write - Performing operation
# 3)Close the file

'''Opening a file
Python provides an open() function that accepts two arguments, file name and access mode in which the file is accessed. 
The function returns a file object which can be used to perform various operations like reading, writing, etc.'''

'''
1	r	It opens the file to read-only mode. The file pointer exists at the beginning. 
        The file is by default open in this mode if no access mode is passed.
2	rb	It opens the file to read-only in binary format. The file pointer exists at the beginning of the file.
3	r+	It opens the file to read and write both. The file pointer exists at the beginning of the file.
4	rb+	It opens the file to read and write both in binary format. The file pointer exists at the beginning of the file.
5	w	It opens the file to write only. It overwrites the file if previously exists or creates a new one if no file exists with the same name. 
        The file pointer exists at the beginning of the file.
6	wb	It opens the file to write only in binary format. It overwrites the file if it exists previously or creates a new one if no file exists. 
        The file pointer exists at the beginning of the file.
7	w+	It opens the file to write and read both. It is different from r+ in the sense that it overwrites the previous file 
        if one exists whereas r+ doesn't overwrite the previously written file. It creates a new file if no file exists. 
        The file pointer exists at the beginning of the file.
8	wb+	It opens the file to write and read both in binary format. The file pointer exists at the beginning of the file.
9	a	It opens the file in the append mode. The file pointer exists at the end of the previously written file if exists any. 
        It creates a new file if no file exists with the same name.
10	ab	It opens the file in the append mode in binary format. The pointer exists at the end of the previously written file. 
        It creates a new file in binary format if no file exists with the same name.
11	a+	It opens a file to append and read both. The file pointer remains at the end of the file if a file exists. 
        It creates a new file if no file exists with the same name.
12	ab+	It opens a file to append and read both in binary format. The file pointer remains at the end of the file.'''


#opens the file file.txt in read mode    
fileptr = open("file.txt","r")    
    
if fileptr:    
    print("file is opened successfully") 
    
    
'''The close() method
Once all the operations are done on the file, we must close it through our Python script using the close() method. 
Any unwritten information gets destroyed once the close() method is called on a file object.'''
# opens the file file.txt in read mode    
fileptr = open("file.txt","r")    
    
if fileptr:    
    print("file is opened successfully")    
    
#closes the opened file    
fileptr.close()  

try:  
   fileptr = open("file.txt")  
   # perform file operations  
finally:  
   fileptr.close()  
   
'''The with statement
The with statement was introduced in python 2.5. The with statement is useful in the case of manipulating the files. 
It is used in the scenario where a pair of statements is to be executed with a block of code in between.'''
# with open(<file name>, <access mode>) as <file-pointer>:    
    #statement suite  
    
with open("file.txt",'r') as f:    
    content = f.read();    
    print(content)    



'''Writing the file
To write some text to a file, we need to open the file using the open method with one of the following access modes.
w: It will overwrite the file if any file exists. The file pointer is at the beginning of the file.
a: It will append the existing file. The file pointer is at the end of the file. It creates a new file if no file exists.'''  

# open the file.txt in append mode. Create a new file if no such file exists.  
fileptr = open("file2.txt", "w")  
fileptr.write('''''Python is the modern day language. It makes things so simple. 
It is the fastest-growing programing language''')  
fileptr.close()  


#Example2
#open the file.txt in write mode.    
fileptr = open("file2.txt","a")  
fileptr.write(" Python has an easy syntax and user-friendly interaction.")        
fileptr.close()  


# Example
#open the file.txt in read mode. causes error if no such file exists.    
fileptr = open("file2.txt","r")  
#stores all the data of the file into the variable content    
content = fileptr.read(10)   
# prints the type of the data stored in the file    
print(type(content))      
#prints the content of the file    
print(content)       
#closes the opened file    
fileptr.close()  

content = fileptr.read()  
print(content)   


# Read file through for loop
# We can read the file using for loop. Consider the following example.
#open the file.txt in read mode. causes an error if no such file exists.    
fileptr = open("file2.txt","r");     
#running a for loop     
for i in fileptr:    
    print(i) # i contains each line of the file    
    
    
'''Read Lines of the file
Python facilitates to read the file line by line by using a function readline() method. 
The readline() method reads the lines of the file from the beginning, i.e., 
if we use the readline() method two times, then we can get the first two lines of the file.'''
# Example 1: Reading lines using readline() function
#open the file.txt in read mode. causes error if no such file exists.    
fileptr = open("file2.txt","r");     
#stores all the data of the file into the variable content    
content = fileptr.readline()     
content1 = fileptr.readline()  
#prints the content of the file    
print(content)     
print(content1)  
#closes the opened file    
fileptr.close()        

# We called the readline() function two times that's why it read two lines from the file.
# Python provides also the readlines() method which is used for the reading lines. 
# It returns the list of the lines till the end of file(EOF) is reached.


# Example 2: Reading Lines Using readlines() function
#open the file.txt in read mode. causes error if no such file exists.    
fileptr = open("file2.txt","r");     
    
#stores all the data of the file into the variable content    
content = fileptr.readlines()     
  
#prints the content of the file    
print(content)     
    
#closes the opened file    
fileptr.close() 


'''Creating a new file
The new file can be created by using one of the following access modes with the function open().
x: it creates a new file with the specified name. It causes an error a file exists with the same name.
a: It creates a new file with the specified name if no such file exists. 
   It appends the content to the file if the file already exists with the specified name.
w: It creates a new file with the specified name if no such file exists. It overwrites the existing file.'''
# Example 1
#open the file.txt in read mode. causes error if no such file exists.    
fileptr = open("file2.txt","x")   
print(fileptr)    
if fileptr:    
    print("File created successfully")  
    
    
'''File Pointer positions
Python provides the tell() method which is used to print the byte number at which the file pointer currently exists. '''
# open the file file2.txt in read mode    
fileptr = open("file2.txt","r")    
#initially the filepointer is at 0     
print("The filepointer is at byte :",fileptr.tell())    
#reading the content of the file    
content = fileptr.read();        
#after the read operation file pointer modifies. tell() returns the location of the fileptr.        
print("After reading, the filepointer is at:",fileptr.tell())        


'''Modifying file pointer position
In real-world applications, sometimes we need to change the file pointer location externally since we may need to read or 
write the content at various locations.
For this purpose, the Python provides us the seek() method which enables us to modify the file pointer position externally.'''
# Syntax:-
# <file-ptr>.seek(offset[, from)    
'''The seek() method accepts two parameters:
offset: It refers to the new position of the file pointer within the file.
from: It indicates the reference position from where the bytes are to be moved. If it is set to 0, 
the beginning of the file is used as the reference position. If it is set to 1, the current position of the 
file pointer is used as the reference position. If it is set to 2, the end of the file pointer is used as the reference position.'''

# open the file file2.txt in read mode    
fileptr = open("file2.txt","r")     
#initially the filepointer is at 0     
print("The filepointer is at byte :",fileptr.tell())    
#changing the file pointer location to 10.    
fileptr.seek(10);    
#tell() returns the location of the fileptr.     
print("After reading, the filepointer is at:",fileptr.tell())    




'''Python OS module
Renaming the file
The Python os module enables interaction with the operating system. 
The os module provides the functions that are involved in file processing operations like renaming, deleting, etc. 
It provides us the rename() method to rename the specified file to a new name. The syntax to use the rename() method is given below.'''

# Syntax:
# rename(current-name, new-name)    
# The first argument is the current file name and the second argument is the modified name. 
# We can change the file name bypassing these two arguments.

import os     
#rename file2.txt to file3.txt    
os.rename("file2.txt","file3.txt")  


'''Creating the new directory
The mkdir() method is used to create the directories in the current working directory. 
The syntax to create the new directory is given below.'''

# Syntax:

# mkdir(directory name)  
# Example 1

import os    
#creating a new directory with the name new    
os.mkdir("new")    


'''The getcwd() method
This method returns the current working directory.'''
import os  
os.getcwd() 


'''Changing the current working directory
The chdir() method is used to change the current working directory to a specified directory.'''

import os   
# Changing current directory with the new directiory  
os.chdir("C:\\Users\\DEVANSH SHARMA\\Documents")  
#It will display the current working directory  
os.getcwd()  

# Deleting directory
import os  
#removing the new directory     
os.rmdir("directory_name")   
