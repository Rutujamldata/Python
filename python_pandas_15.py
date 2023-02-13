# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 10:21:53 2023

@author: rutuja
"""

# Pandas is a Python library.
# Pandas is used to analyze data.

'''To install the pandas !pip install pandas - cmd/console
and to use the pandas import pandas as pd'''



import pandas as pd
df = pd.read_csv('C:/Users/user/Downloads/Courses.CSV')
print(df.to_string())


# Pandas allows us to analyze big data and make conclusions based on statistical theories.
# Pandas can clean messy data sets, and make them readable and relevant.
# Relevant data is very important in data science. 

import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)



import pandas as pd
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)
print(myvar)


##Checking Pandas version
import pandas as pd
print(pd.__version__)


##A Pandas Series is like a column in a table.
##It is a one-dimensional array holding data of any type.
import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)
print(myvar[0])


# Create a simple Pandas Series from a dictionary:
import pandas as pd
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)

#Create a Series using only data from "day1" and "day2":
import pandas as pd
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories, index = ["day1", "day2"])
print(myvar)


#Create Labels
import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)
print(myvar["y"])


#Create a DataFrame from two Series:
import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data)
print(myvar)


#A Pandas DataFrame is a 2 dimensional data structure, 
# like a 2 dimensional array, or a table with rows and columns.
import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
#load data into a DataFrame object:
df = pd.DataFrame(data)
print(df) 

#refer to the row index:
print(df.loc[0])

# Return row 0 and 1:

#use a list of indexes:
print(df.loc[[0, 1]])
print(df.loc[[0,2]])


# Add a list of names to give each row a name:
import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df) 

#refer to the named index:
print(df.loc["day2"])
