# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 10:50:34 2023

@author: rutuja
"""

data = [{'Rank': 'B', 'first_name': 'Parker', 'last_name': 'Brian'},     
{'Rank': 'A', 'first_name': 'Smith', 'last_name': 'Rodriguez'},    
{'Rank': 'C', 'first_name': 'Tom', 'last_name': 'smith'},    
{'Rank': 'B', 'first_name': 'Jane', 'last_name': 'Oscar'},     
{'Rank': 'A', 'first_name': 'Alex', 'last_name': 'Tim'}]   

import csv    
     
with open('Python.csv', 'w') as csvfile:    
    fieldnames = ['first_name', 'last_name', 'Rank']    
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)    
     
    writer.writeheader()    
    writer.writerow({'Rank': 'B', 'first_name': 'Parker', 'last_name': 'Brian'})    
    writer.writerow({'Rank': 'A', 'first_name': 'Smith',    
                     'last_name': 'Rodriguez'})    
    writer.writerow({'Rank': 'B', 'first_name': 'Jane', 'last_name': 'Oscar'})    
    writer.writerow({'Rank': 'B', 'first_name': 'Jane', 'last_name': 'Loive'})    
     
print("Writing complete")    



#write csv into dict
import csv    
with open('python.csv', mode='w') as csv_file:    
    fieldnames = ['emp_name', 'dept', 'birth_month']    
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)    
    writer.writeheader()    
    writer.writerow({'emp_name': 'Parker', 'dept': 'Accounting', 'birth_month': 'November'})    
    writer.writerow({'emp_name': 'Smith', 'dept': 'IT', 'birth_month': 'October'})   
    
    
    
#write csv files into pandas
import pandas    
df = pandas.read_csv('hrdata.csv',     
            index_col='Employee',     
            parse_dates=['Hired'],    
            header=0,     
            names=['Employee', 'Hired', 'Salary', 'Sick Days'])    
df.to_csv('hrdata_modified.csv')      
