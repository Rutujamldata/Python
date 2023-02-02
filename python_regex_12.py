# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 15:44:53 2023

@author: user
"""

#Python Regex

'''A regular expression is a set of characters with highly specialized syntax that 
we can use to find or match other characters or groups of characters. In short, 
regular expressions, or Regex, are widely used in the UNIX world.'''

#Parameters
'''pattern:- this is the expression that is to be matched. It must be a regular expression

string:- This is the string that will be compared to the pattern at the start of the string.

flags:- Bitwise OR (|) can be used to express multiple flags. These are modifications, 
        and the table below lists them.'''
        
#To use regex function in python we need to import the library "import re"

import re  
line = "Learn Python through tutorials on javatpoint"  
match_object = re.match( r'.w* (.w?) (.w*?)', line, re.M|re.I)  
  
if match_object:  
    print ("match object group : ", match_object.group())  
    print ("match object 1 group : ", match_object.group(1))  
    print ("match object 2 group : ", match_object.group(2))  
else:  
    print ( "There isn't any match!!" )          


import re  
line = "Learn Python through tutorials"  
  
match_object = re.match( r'through', line, re.M|re.I)  
if match_object:  
    print("match object group : ", match_object.group())  
else:  
    print( "There isn't any match!!")  
  
search_object = re.search( r' .*t? ', line, re.M|re.I)  
if search_object:  
    print("search object group : ", search_object.group())  
else:  
    print("Nothing found!!")  

#Example findall
import re
s = "black, blue and brown"
pattern = r'bl\w+'
matches = re.findall(pattern,s)
print(matches)


#Example
import re
s = "black, blue and brown"
pattern = r'bl(\w+)'
matches = re.findall(pattern,s)
print(matches)


#Examples
target_string = "Emma is a basketball player who was born on June 17, 1993. She played 112 matches with scoring average 26.12 points per game. Her weight is 51 kg."
result = re.findall(r"\d+", target_string)
print("Found following matches")
print(result)


#Metacharacters
'''
[]	A set of characters	"[a-m]"	
\	Signals a special sequence (can also be used to escape special characters)	"\d"	
.	Any character (except newline character)	"he..o"	
^	Starts with	"^hello"	
$	Ends with	"planet$"	
*	Zero or more occurrences	"he.*o"	
+	One or more occurrences	"he.+o"	
?	Zero or one occurrences	"he.?o"	
{}	Exactly the specified number of occurrences	"he.{2}o"	
|	Either or	"falls|stays"
'''

#Special Sequence
'''
\A	Returns a match if the specified characters are at the beginning of the string	"\AThe"	
\b	Returns a match where the specified characters are at the beginning or at the end of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"
r"ain\b"	
\B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"
r"ain\B"	
\d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	
\D	Returns a match where the string DOES NOT contain digits	"\D"	
\s	Returns a match where the string contains a white space character	"\s"	
\S	Returns a match where the string DOES NOT contain a white space character	"\S"	
\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
\W	Returns a match where the string DOES NOT contain any word characters	"\W"	
\Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"
'''



#set
'''
[arn]	Returns a match where one of the specified characters (a, r, or n) is present	
[a-n]	Returns a match for any lower case character, alphabetically between a and n	
[^arn]	Returns a match for any character EXCEPT a, r, and n	
[0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	Returns a match for any digit between 0 and 9	
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any +
'''

#Example findall
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

#Example Search 
txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())


#Example split function
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
