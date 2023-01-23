# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 11:57:58 2023

@author: rutuja
"""
'''
Variables can hold values, and every value has a data-type. Python is a dynamically typed language; 
hence we do not need to define the type of the variable while declaring it. 
The interpreter implicitly binds the value with its type.
'''
#int
a = 5
#float
b = 1.2
#complex
d = 4 + 9j

#datatype of that variables
type(a)
type(b)
type(d)


#string
c = 'python'
c1 = '''python
        c prog
        c ++ '''
        
type(c)
type(c1)      

str1 = 'hello javatpoint' #string str1    
str2 = ' how are you' #string str2    

#Slicing
print (str1[0:2]) #printing first two character using slice operator    
print (str1[4]) #printing 4th character of the string    


print (str1*2) #printing the string twice    
print (str1 + str2) #printing the concatenation of str1 and str2    


#List
'''Python Lists are similar to arrays in C. However, the list can contain data of different types. 
The items stored in the list are separated with a comma (,) and enclosed within square brackets [].'''

list1  = [1, "hi", "Python", 2]    
#Checking type of given list  
print(type(list1))  
  
#Printing the list1  
print (list1)  
  
# List slicing  
print (list1[3:])  
  
# List slicing  
print (list1[0:2])   
  
# List Concatenation using + operator  
print (list1 + list1)  
  
# List repetation using * operator  
print (list1 * 3)  

#append data in list
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")

a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)

#Clear list
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()

# Copy list from one to another variable
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()

# Return the number of times the value "cherry" appears in the fruits list:

fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")

points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)

#The extend() method adds the specified list elements (or any iterable) to the end of the current list.
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)


#Add a tuple to the fruits list:
fruits = ['apple', 'banana', 'cherry']
points = (1, 4, 5, 9)
fruits.extend(points)

# index for that particular element
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")

# Insert element in the dict 1 defines that where i want to store that element in the list 
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")

#If i want to delete the element from particular index the we will use the pop method
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)

#The remove() method removes the first occurrence of the element with the specified value.
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")

fruits = ['apple', 'banana', 'cherry','banana']
fruits.remove("banana")

#Revers the List
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()

#sort the list
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()

#sort in descending order
cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)

#sort a list according to year
# A function that returns the 'year' value:
def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)

#Tuple
'''A tuple is similar to the list in many ways. Like lists, tuples also contain the collection of the items of different data types. 
The items of the tuple are separated with a comma (,) and enclosed in parentheses ().
A tuple is a read-only data structure as we can't modify the size and value of the items of a tuple.'''

tup  = ("hi", "Python", 2)    
# Checking type of tup  
print (type(tup))    
  
#Printing the tuple  
print (tup)  
  
# Tuple slicing  
print (tup[1:])    
print (tup[0:1])    
  
# Tuple concatenation using + operator  
print (tup + tup)    
  
# Tuple repatation using * operator  
print (tup * 3)     
  
# Adding value to tup. It will throw an error.  
tup[2] = "hi" 

'''Traceback (most recent call last):

  Cell In[43], line 19
    tup[2] = "hi"

TypeError: 'tuple' object does not support item assignment'''


#count for the particular element in tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)

#Index in tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)

#Dictionary
'''Dictionary is an unordered set of a key-value pair of items. It is like an associative array or a hash table where 
each key stores a specific value. Key can hold any primitive data type, whereas value is an arbitrary Python object.
The items in the dictionary are separated with the comma (,) and enclosed in the curly braces {}.'''

d = {1:'Jimmy', 2:'Alex', 3:'john', 4:'mike'}     
  
# Printing dictionary  
print (d)  
  
# Accesing value using keys  
print("1st name is "+d[1])   
print("2nd name is "+ d[4])    
  
print (d.keys())    
print (d.values()) 

#Copy Dict
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.copy()

print(x)

#Form keys dict
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)

#get values of the key
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")

print(x)


# Try to return the value of an item that do not exist:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.get("price", 15000)

print(x)
car

#Return items of the dictionary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

print(x)


# When an item in the dictionary changes value, the view object also gets updated:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

car["year"] = 2018

print(x)

# here we get the keys of the dict
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()

print(x)

# here we get the values of the dict
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()

print(x)

#pop from the dict
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.pop("model")

print(car)

#pop items from the dict
'''The popitem() method removes the item that was last inserted into the dictionary. 
In versions before 3.7, the popitem() method removes a random item.
The removed item is the return value of the popitem() method, as a tuple'''
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.popitem()

print(car)

#set default value in dict
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "white")

print(x)


#The update() method inserts the specified items to the dictionary.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})

print(car)



# Boolean
# Boolean type provides two built-in values, True and False. These values are used to determine the given statement true or false. 
# It denotes by the class bool. True can be represented by any non-zero value or 'T' whereas false can be represented by the 0 or 'F'.
print(type(True))  
print(type(False))  
print(false)  
'''Traceback (most recent call last):

  Cell In[94], line 3
    print(false)

NameError: name 'false' is not defined'''

#set
'''Python Set is the unordered collection of the data type. It is iterable, mutable(can modify after creation), and has unique elements.
 In set, the order of the elements is undefined; it may return the changed sequence of the element. 
 The set is created by using a built-in function set(), or a sequence of elements is passed in the curly braces and separated by the comma. 
 It can contain various types of values. '''
 
 # Creating Empty set  
set1 = set()  
  
set2 = {'James', 2, 3,'Python'}  
  
#Printing Set value  
print(set2)  
  
# Adding element to the set  
  
set2.add(10)  
print(set2)  
  
#Removing element from the set  
set2.remove(2)  
print(set2)  


#Add elements to set
'''The add() method adds an element to the set.
If the element already exists, the add() method does not add the element.'''
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)


#clear the set
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)

#Copy set from one 
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)


#differenc from to sets
# from X set
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)

# From Y set
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = y.difference(x)
print(z)


'''The difference_update() method removes the items that exist in both sets.
The difference_update() method is different from the difference() method, because the difference() method returns a new set, 
without the unwanted items, and the difference_update() method removes the unwanted items from the original set.'''

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)


'''The discard() method removes the specified item from the set.
This method is different from the remove() method, because the remove() method will raise an error if the specified item does not exist,
 and the discard() method will not.'''
 
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits) 

# Set intersection {Find out similar element}
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
result = x.intersection(y, z)
print(result)



# The intersection_update() method is different from the intersection() method, because the intersection() method returns a new set, 
# without the unwanted items, and the intersection_update() method removes the unwanted items from the original set.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
x.intersection_update(y, z)
print(x)


# The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.isdisjoint(y)
print(z)


#subset
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b"}
z = x.issubset(y)
print(z)

#Super set
#The issuperset() method returns True if all items in the specified set exists in the original set, otherwise it retuns False.

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)

x = {"f", "e", "d", "c", "b"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)

#pop Complete sets 
fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)

fruits = {"apple", "banana", "cherry"}
x = fruits.pop()
print(x)

#Remove single item from the sets
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)


#symmetric Difference 
# The symmetric_difference() method returns a set that contains all items from both set, 
# but not the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

#Symmetric Differenc Update
# The symmetric_difference_update() method updates the original set by removing items that are present in both sets, 
# and inserting the other items.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

#Sets Union(show thw all elements from both the set only duplicates are not allow)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)

x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}
result = x.union(y, z)
print(result)

#update in sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x)
