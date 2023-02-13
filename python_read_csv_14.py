# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 10:06:38 2023

@author: rutuja
"""
#Read csv into list
import csv
 
# opening the CSV file
with open("C:/Users/user/Downloads/Courses.CSV", mode ='r')as file:
   
  # reading the CSV file
  csvFile = csv.reader(file)
 
  # displaying the contents of the CSV file
  for lines in csvFile:
        print(lines)
        
        
        
#Read csv into dict        
import csv

myFile = open('C:/Users/user/Downloads/Courses.CSV', 'r')
reader = csv.DictReader(myFile)
myList = list()
for dictionary in reader:
    myList.append(dictionary)
print("The list of dictionaries is:")
print(myList)        


