# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 14:43:25 2023

@author: rutuja
"""

# Stack works on the principle of “Last-in, first-out”. 
# Also, the inbuilt functions in Python make the code short and simple. 
# To add an item to the top of the list, i.e., to push an item, 
# we use append() function and to pop out an element we use pop() function.
stack = ["Amar", "Akbar", "Anthony"]
stack.append("Ram")
stack.append("Iqbal")
print(stack) 
# Removes the last item
print(stack.pop())
print(stack)
# Removes the last item
print(stack.pop()) 
print(stack)



# Queue works on the principle of “First-in, first-out”. 
# Below is list implementation of queue. 
# We use pop(0) to remove the first item from a list.
# Python code to demonstrate Implementing 
# Queue using list
queue = ["Amar", "Akbar", "Anthony"]
queue.append("Ram")
queue.append("Iqbal")
print(queue)
# Removes the first item
print(queue.pop(0))
print(queue)
# Removes the first item
print(queue.pop(0))
print(queue)



# Using Deque
# In case of stack, list implementation works fine and provides both append() 
# and pop() in O(1) time. When we use deque implementation, we get same time complexity.


# Python code to demonstrate Implementing 
# Stack using deque
from collections import deque
queue = deque(["Ram", "Tarun", "Asif", "John"])
print(queue)
queue.append("Akbar")
print(queue)
queue.append("Birbal")
print(queue)
print(queue.pop())                 
print(queue.pop())                 
print(queue)
