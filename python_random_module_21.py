# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 12:29:39 2023

@author: rutuja
"""

#Random module

'''The random.random() function gives a float number that ranges from 0.0 to 1.0. 
There are no parameters required for this function.'''
import random  
num=random.random()  
print(num)  

import random  
num = random.randint(1, 500)  
print( num )

#Generate Random Numbers within a Defined Range
import random  
  
num = random.randrange(1, 10)  
print( num )  
num = random.randrange(1, 10, 2)  
print( num )              
num = random.randrange(0, 101, 10)  
print( num ) 

#Select Random Elements
import random  
random_s = random.choice('Random Module') #a string  
print( random_s )  
random_l = random.choice([23, 54, 765, 23, 45, 45]) #a list  
print( random_l )  
random_s = random.choice((12, 64, 23, 54, 34)) #a set  
print( random_s )  

# Shuffle Elements Randomly
a_list = [34, 23, 65, 86, 23, 43]  
random.shuffle( a_list )  
print( a_list )  
random.shuffle( a_list )  
print( a_list ) 

# Random Seed
'''We normally use the time of the system to ensure that the software delivers a 
different output each time we execute it because pseudorandom synthesis is 
dependent on the preceding number. As a result, we employ seeds.'''
import random   
random.seed(2)   
print('Generating 5 random numbers: ')  
print([ random.randint(1, 300) for r in range(6)])  
   
# Reseting the seed value to 1  
random.seed(2)  
   
# We will get the same numbers as before  
print([random.randint(1, 300) for i in range(6)])  


'''
seed(a=None, version=2)	This function creates a new random number.
getstate()	This method provides an object reflecting the generator's present state. Provide the argument to setstate() to recover the state.
setstate(state)	Providing the state object resets the function's state at the time getstate() was invoked.
getrandbits(k)	This function provides a Python integer having k random bits. This is important for random number production algorithms like randrange(), which can manage arbitrarily huge ranges.
randrange(start, stop[, step])	From the range, it produces a random integer.
randint(a, b)	Provides an integer within a and b at random (both inclusive). If a > b, a ValueError is thrown.
choice(seq)	Produce a non-empty series item at random.
shuffle(seq)	Change the order.
sample(population, k)	Display a list of k-size unique entries from the population series.
random()	This function creates a new random number.
uniform(a, b)	This method provides an object reflecting the generator's present state. Provide the argument to setstate() to recover the state.
triangular(low, high, mode)	Providing the state object resets the function's state at the time getstate() was invoked.
betavariate(alpha, beta)	Beta distribution
expovariate(lambd)	Exponential distribution
gammavariate(alpha, beta)	Gamma distribution
gauss(mu, sigma)	Gaussian distribution
lognormvariate(mu, sigma)	Log normal distribution
normalvariate(mu, sigma)	Normal distribution
vonmisesvariate(mu, kappa)	Vonmises distribution
paretovariate(alpha)	Pareto distribution
weibullvariate(alpha, beta)	Weibull distribution
'''
