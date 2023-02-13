# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 12:46:04 2023

@author: user
"""

''''To add "magic" to the class we create, we can define special methods called "magic methods." 
For example, the magic methods __init__ and __str__are always wrapped by double underscores from both sides. 
By granting us accessibility to Python's built-in syntax tools, magic methods can improve the structure 
of our classes.

''We can integrate Pythons built-in classes with our classes. The class which has 
inherited from the built-in class is known as a child class. A child class has access to 
all of the attributes of the parent class, including its methods. By utilizing the essential 
built-in features, we can customize some of the tasks of our class by using magic methods.'''

# Python program to show how __init__ method works  
  
# Creating a class  
class methods():  
    def __init__(self, *args):  
        print ("Now called __init__ magic method, after tha initialised parameters")  
        self.name = args[0]  
        self.std = args[1]  
        self.marks = args[2]  
  
Student = methods("Itika", 11, 98)  
print(Student)  
print(f"Name, standard, and marks of the student is: \n", Student.name, "\n", Student.std, "\n", Student.marks)  



'''__new__() Method
The magic method __new__() is called implicitly by the __init__() method. 
The new instance returned by the __new__() method is initialised. 
To modify the creation of objects in a user-defined class, we must supply a 
modified implementation of the __new__() magic method. We need to provide the 
first argument as the reference to the class whose object is to be created for this static function.'''

# Python program to show how __new__ method works  
    
# Creating a class  
class Method(object):  
    def __new__( cls ):  
        print( "Creating an instance by __new__ method")  
        return super(Method, cls).__new__(cls)  
    # Calling the init method  
    def __init__( self ):  
        print( "Init method is called here" )  
  
Method()  



# Python program to show how to add two attributes  
  
# Creating a class  
class Method:  
    def __init__(self, argument):  
        self.attribute = argument  
  
# Creating a second class  
class Method_2:  
    def __init__(self, argument):  
        self.attribute = argument  
# creating the instances  
instance_1 = Method(" Attribute")  
print(instance_1.attribute)  
instance_2 = Method_2(" 27")  
print(instance_2.attribute)  
  
# Adding two attributes of the instances  
print(instance_2.attribute + instance_1.attribute) 


# Python program to show how __add__ method works  
  
# Creating a class  
class Method:  
    def __init__(self, argument):  
        self.attribute = argument  
    def __add__(self, object1):  
        return self.attribute + object1.attribute  
  
# Creating a second class  
class Method_2:  
    def __init__(self, argument):  
        self.attribute = argument  
    def __add__(self, object1):  
        return self.attribute + object1.attribute  
instance_1 = Method(" Attribute")  
print(instance_1)  
instance_2 = Method_2(" 27")  
print(instance_2)  
print(instance_2 + instance_1)  



# Python program to show how __repr__ magic method works  
  
# Creating a class  
class Method:  
    # Calling __init__ method and initializing the attributes of the class  
    def __init__(self, x, y, z):  
        self.x = x  
        self.y = y  
        self.z = z  
    # Calling the __repr__ method and providing the string to be printed each time instance is printe  
    def __repr__(self):  
        return f"Following are the values of the attributes of the class Method:\nx = {self.x}\ny = {self.y}\nz = {self.z}"  
instance = Method(4, 6, 2)  
print(instance)  


# Python code to show how the __contains__ magic method works  
  
# Creating a class  
class Method:  
    # Calling the __init__ method and initializing the attributes  
    def __init__(self, attribute):  
        self.attribute = attribute  
          
    # Calling the __contains__ method  
    def __contains__(self, attribute):  
        return attribute in self.attribute  
# Creating an instance of the class  
instance = Method([4, 6, 8, 9, 1, 6])  



# Python program to show how the __call__ magic method works  
  
# Creating a class  
class Method:  
    # Calling the __init__ method and initializing the attributes  
    def __init__(self, a):  
        self.a = a  
    # Calling the __call__ method to multiply a number to the attribute value  
    def __call__(self, number):  
        return self.a * number  
  
# Creating an instance and proving the value to the attribute a  
instance = Method(7)  
print(instance.a) # Printing the value of the attribute a  
# Calling the instance while passing a value which will call the __call__ method  
print(instance(5))  
  
# Checking if a value is present in the container attribute  
print("4 is contained in ""attribute"": ", 4 in instance)  
print("5 is contained in ""attribute"": ", 5 in instance)  



# Python program to show how the __iter__ method works  
  
# Creating a class  
class Method:  
    def __init__(self, start_value, stop_value):  
        self.start = start_value  
        self.stop = stop_value  
    def __iter__(self):  
        for num in range(self.start, self.stop + 1):  
            yield num ** 2  
# Creating an instance  
instance = iter(Method(3, 8))  
print( next(instance) )  
print( next(instance) )  
print( next(instance) )  
print( next(instance) )  
print( next(instance) )  
print( next(instance) )
