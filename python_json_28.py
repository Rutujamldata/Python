# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 12:38:11 2023

@author: rutuja
"""

import json  
# Key:value mapping  
student  = {  
"Name" : "Peter",  
"Roll_no" : "0090014",  
"Grade" : "A",  
"Age": 20,  
    "Subject": ["Computer Graphics", "Discrete Mathematics", "Data Structure"]  
}  
  
with open("data.json","w") as write_file:  
    json.dump(student,write_file)
    
'''The dumps() function is used to store serialized data in the Python file. 
It accepts only one argument that is Python data for serialization. 
The file-like argument is not used because we aren't not writing data to disk.'''
    
import json  
# Key:value mapping  
student  = {  
"Name" : "Peter",  
"Roll_no" : "0090014",  
"Grade" : "A",  
"Age": 20  
}  
b = json.dumps(student)  
  
print(b)      

  
#Python  list conversion to JSON  Array   
print(json.dumps(['Welcome', "to", "javaTpoint"]))  
  
#Python  tuple conversion to JSON Array   
print(json.dumps(("Welcome", "to", "javaTpoint")))  
  
# Python string conversion to JSON String   
print(json.dumps("Hello"))  
  
# Python int conversion to JSON Number   
print(json.dumps(1234))  
  
# Python float conversion to JSON Number   
print(json.dumps(23.572))  
  
# Boolean conversion to their respective values   
print(json.dumps(True))  
print(json.dumps(False))  
  
# None value to null   
print(json.dumps(None))   



'''Deserializing JSON
Deserialization is the process to decode the JSON data into the Python 
objects. The json module provides two methods load() and loads(), 
which are used to convert JSON data in actual Python object form.'''


import json  
a = (10,20,30,40,50,60,70)  
print(type(a))  
b = json.dumps(a)  
print(type(json.loads(b)))  


# The load() function
'''The load() function is used to deserialize the JSON data to Python 
object from the file. Consider the following example:'''

import json  
# Key:value mapping  
student  = {  
"Name" : "Peter",  
"Roll_no" : "0090014",  
"Grade" : "A",  
"Age": 20,  
}  
  
with open("data.json","w") as write_file:  
    json.dump(student,write_file)  
  
with open("data.json", "r") as read_file:  
    b = json.load(read_file)  
print(b)  



import json  
a = ["Mathew","Peter",(10,32.9,80),{"Name" : "Tokyo"}]  
  
# Python object into JSON   
b = json.dumps(a)  
  
# JSON into Python Object  
c = json.loads(b)  
print(c)


# json.load() vs json.loads()
'''The json.load() function is used to load JSON file, 
whereas json.loads() function is used to load string.'''

# json.dump() vs json.dumps()
'''The json.dump() function is used when we want to serialize the Python 
objects into JSON file and json.dumps() function is used to convert 
JSON data as a string for parsing and printing.'''


import json  
  
person = '{"Name": "Andrew","City":"English", "Number":90014, "Age": 23,"Subject": ["Data Structure","Computer Graphics", "Discrete mathematics"]}'  
per_dict = json.loads(person)  
print(json.dumps(per_dict, indent = 5, sort_keys= True))  

  
