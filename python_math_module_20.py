# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 12:19:06 2023

@author: rutuja
"""

# importing the math module  
import math  
print(math.sqrt( 9 ))  

import math  
print( "The value of Euler's Number is: ", math.e )  

import math  
print ( "The value of Tau is: ", math.tau ) 

import math  
print( math.inf )  
print( -math.inf )  


import math  
print( math.inf > 10e109 )  
print( -math.inf < -10e109 )  

import math  
print( "The value of pi is ", math.pi )  


import math  
# radius of the circle  
r = 4  
# value of pi  
pi_value = math.pi  
# circumference of the circle  
print(2 * pi_value * r)  

import math  
# Printing the value of nan using the math module  
print( math.nan )  


import math  
x = 4.346  
# returning the ceiling value of 4.346  
print("The ceiling value of 4.346 is : ", end="")  
print( math.ceil(x) )  
   
# returning the floor value of 4.346  
print("The floor value of 4.346 is : ", end="")  
print( math.floor(x) )  


#Find out the factorial of the number
import math  
x = 6  
# returning the factorial of 6  
print( "The factorial of 6 is : ", math.factorial(x) )  
  
try:  
    print( "The factorial of 6.5 in: ", math.factorial(6.5) )  
except:  
    print( "Cannot calculate factorial of a non-integral number" )
    
    
    
#Exponential value
import math  
# declaring some value  
num1 = 4  
num2 = -3  
num3 = 0.00  
# passing above values to the exp() function  
print( f"The exponenetial value of {num1} is: ", math.exp(num1) )  
print( f"The exponenetial value of {num2} is: ", math.exp(num2) )  
print( f"The exponenetial value of {num3} is: ", math.exp(num3) )      

## Power of the number
import math  
x = 4  
y = 5  
# returning x to the power of y.  
print( f"The value of {x} to the power of {y} is: ", math.pow(x,y) )  



# Python program to show how to use the sin(), cos(), tan() function.  
import math  
angle = math.pi / 4  
   
# returning the sine of pi/4  
print( "The sine of pi/4 is : ", math.sin( angle ) )  
   
# returning the cosine of pi/4  
print( "The cosine of pi/4 is : ", math.cos( angle ) )  
   
# returning the tangent of pi/4  
print("The tangent of pi/4 is : ", math.tan( angle ))  

math.asinh(angle)

'''
ceil(x)	The lowest integer bigger than or equal to x is returned.
copysign(x, y)	gives x back with the sign of y.
fabs(x)	gives x's absolute value back.
factorial(x)	provides the x factorial back.
floor(x)	gives back the biggest integer that is less than or equal to x.
fmod(x, y)	returns the leftover value after dividing x by y.
frexp(x)	returns the pair of the mantissa and exponent of x. (m, e)
fsum(iterable)	returns the iterable's correct floating point sum of all values.
isfinite(x)	If x is neither an infinity nor a NaN, it returns True (Not a Number)
isinf(x)	If x is a positive or negative infinity, it returns True.
isnan(x)	If x is a NaN, it returns True.
ldexp(x, i)	gives back x * (2**i).
modf(x)	gives x's fractional and integer components back.
trunc(x)	x's shortened integer value is returned.
exp(x)	delivers e**x
expm1(x)	yields e**x - 1
log(x[, b])	gives back the x logarithm in base b. (defaults to e)
log1p(x)	the natural logarithm of 1 + x is returned.
log2(x)	gives x's base-2 logarithm back.
log10(x)	provides x's base-10 logarithm.
pow(x, y)	gives x raised to the power of y back.
sqrt(x)	gives x's square root back.
acos(x)	gives the arc cosine of x back.
asin(x)	gives the arc sine of x back.
atan(x)	gives the arc tangent of x back.
atan2(y, x)	gives back atan(y / x).
cos(x)	returns the x's cosine.
hypot(x, y)	returns sqrt(x*x + y*y), the Euclidean norm.
sin(x)	gives the sine of x back.
tan(x)	gives the tangent of x back.
degrees(x)	Angle x is transformed from radians to degrees.
radians(x)	Angle x is transformed from degrees to radians.
acosh(x)	x's inverse hyperbolic cosine is returned.
asinh(x)	x's inverse hyperbolic sine is returned.
atanh(x)	x's inverse hyperbolic tangent is returned.
cosh(x)	gives x's hyperbolic cosine.
sinh(x)	gives x's hyperbolic cosine.
tanh(x)	gives x's hyperbolic tangent back.
erf(x)	the error function at x is returned.
erfc(x)	a function that gives the complementary error at x
gamma(x)	the Gamma function at x is returned.
lgamma(x)	gives the natural logarithm of the gamma function's absolute value at x.
pi	The ratio of a circle's circumference to its diameter is a mathematical constant (3.14159...)
e	e is a constant in mathematics (2.71828...)'''
