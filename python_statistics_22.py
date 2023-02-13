# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 12:35:29 2023

@author: user
"""
##Mean
import statistics    
# list of positive integer numbers   
datasets = [5, 2, 7, 4, 2, 6, 8]     
x = statistics.mean(datasets)     
# Printing the mean   
print("Mean is :", x)  

#Median
import statistics     
datasets = [4, -5, 6, 6, 9, 4, 5, -2]      
# Printing median of the   
# random data-set   
print("Median of data-set is : % s "  
        % (statistics.median(datasets)))  

#Mode
import statistics     
# declaring a simple data-set consisting of real valued positive integers.   
dataset =[2, 4, 7, 7, 2, 2, 3, 6, 6, 8]     
# Printing out the mode of given data-set   
print("Calculated Mode % s" % (statistics.mode(dataset)))  


#standard deviations
import statistics     
# creating a simple data - set   
sample = [7, 8, 9, 10, 11]     
# Prints standard deviation   
print("Standard Deviation of sample is % s "   
                % (statistics.stdev(sample)))   


#Median Low
import statistics     
# simple list of a set of integers   
set1 = [4, 6, 2, 5, 7, 7]     
# Note: low median will always be a member of the data-set.     
# Print low median of the data-set   
print("Low median of data-set is % s "   
        % (statistics.median_low(set1)))  

#Median High
import statistics     
# list of set of the integers   
dataset = [2, 1, 7, 6, 1, 9]     
print("High median of data-set is %s "   
        % (statistics.median_high(dataset)))  
