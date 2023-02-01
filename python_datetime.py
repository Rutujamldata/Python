# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 12:49:33 2023

@author: user
"""

'''Python Date and time'''
# Python provides the datetime module work with real dates and times. 
# In real-world applications, we need to work with the date and time. 
# Python enables us to schedule our Python script to run at a particular timing.

'''date - It is a naive ideal date. It consists of the year, month, and day as attributes.
time - It is a perfect time, assuming every day has precisely 24*60*60 seconds. 
       It has hour, minute, second, microsecond, and tzinfo as attributes.
datetime - It is a grouping of date and time, along with the attributes year, month, day, hour, minute, second, microsecond, and tzinfo.
timedelta - It represents the difference between two dates, time or datetime instances to microsecond resolution.
tzinfo - It provides time zone information objects.
timezone - It is included in the new version of Python. It is the class that implements the tzinfo abstract base class.'''

import time;  
#prints the number of ticks spent since 12 AM, 1st January 1970  
print(time.time())  


'''Current time'''
import time;    
#returns a time tuple     
print(time.localtime(time.time()))  


'''Getting Formatted time'''
import time    
  #returns the formatted time        
print(time.asctime(time.localtime(time.time())))  


'''Python sleep time'''
import time  
for i in range(0,5):  
    print(i)  
    #Each element will be printed after 1 second  
    time.sleep(1)  
    
    
'''The datetime Module    '''

import datetime  
#returns the current datetime object     
print(datetime.datetime.now())   

'''Creating date objects'''
import datetime    
#returns the datetime object for the specified date    
print(datetime.datetime(2020,4,4))   


import datetime     
#returns the datetime object for the specified time        
print(datetime.datetime(2020,4,4,1,26,40))  


'''Comparison of two dates'''
from datetime import datetime as dt    
#Compares the time. If the time is in between 8AM and 4PM, then it prints working hours otherwise it prints fun hours    
if dt(dt.now().year,dt.now().month,dt.now().day,8)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,16):    
    print("Working hours....")    
else:    
    print("fun hours")   



'''The calendar module'''
import calendar    
cal = calendar.month(2020,3)    
#printing the calendar of December 2018    
print(cal) 


'''Printing the calendar of whole year'''
import calendar    
s = calendar.prcal(2020) 


   
