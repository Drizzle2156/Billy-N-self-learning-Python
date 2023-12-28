# String or str data type

# literal assignment is the 1st way to assign str data to a variable
# the type function identifies what class the variable is. In this case "Dave" is a str
import math
first = "Dave"
last = "Gray"

# print(type(first))
# print(type(first) == str)  # is type first equal to a str? outputs true
# print(
#     isinstance(first, str)
# )
#  isinstance function returns True if the specificed object is the specified type
# the object here is first and the specified type is str, so it is True


# pizza = str(
#     "Pepperoni"
# )  # constructor function is a 2nd way to assign str data to a variable besides literal assignments
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))


# Concatenation means adding strings together
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# casting a number to a string. To cast a number to a string in Python, you can use the str() function.
# The str() function takes any Python data type and converts it into a string.
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)


# to get a statement with multiple lines , use 3 quotes. the variable is named multiline in this ex.
# start of multi line
multiline = """ 
Hey how are you?

I was just checking in.
                                All good? 
"""  # end of multi line
# to get the vertical lines above i hit tab.
print(multiline)

# escaping special charachters. To insert characters that are not allowed in a string
# we use \ followed by the character I want to insert. check python escape characters link for full list

sentence = "I'm back at work!\tHey!\n\nWhere's this at\\located?"

print(sentence)

# string methods
print(first)
print(first.lower())  # makes all lower case
print(first.upper())  # makes all upper case
print(first)

print(multiline.title())  # adds an upper case to each work
print(multiline.replace("good", "ok"))  # replaces good with ok
print(multiline)

# len() length function counts every character in the variable
print(len(multiline))
multiline += "                                          "
multiline = "                   " + multiline
# remember that the len() function returns the # of items in an object
print(len(multiline))
# when the object is a string it returns the # of characters in the string

# string methods to remove the extra space. stopped at 1:03:55
print(len(multiline.strip()))  # removes all extra space
print(len(multiline.lstrip()))  # removes all extra space to the left
print(len(multiline.rstrip()))  # removes all extra space to the right
# theres a complete list of string methods in the documentation in course resources

print("")  # this adds an empty line

# build a menu
# the .upper() makes the string all upper case. the .center()
title = "menu".upper()
# center method, pass in 20 characters using an equal sign
print(title.center(20, "="))


# The rjust() method will right align the string, using a specified character (space is default) as the fill character.
# txt = "banana"
# x = txt.rjust(20)
# print(x)
# Note: In the result, there are actually 14 whitespaces to the left of the word banana. the last letter of banana is the 20th character counter from left to right

# for ljust(16, "."), we are using . as the fill character
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

print("")

# string index values
# in python we start counting from 0 for string index values. Dave -> a is 1
print(first[1])
print(first[-1])  # -1 will always give the value in the string, e is last
# [value 1:value 2] gives a range, note that the value you give at the end of the range wont be outputted
print(first[1:-1])
# when you dont provide an end value it will output all to the end
print(first[1:])

# Some methods return boolean data
print(first.startswith("D"))  # true because Dave starts with D
print(first.endswith("Z"))  # this gives false because Dave doesnt end with Z
# hitting . after first will give a dropdown list of all possible functions to work with strings

# boolean data types, which is just True and False
# true and false can only be capital for first letter
myvalue = True
x = bool(False)  # constructor function
print(type(x))  # check the data type for x
print(isinstance(myvalue, bool))  # is myvalue a bool value?

# Numeric data types

# integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, bool))

# float type
gpa = 3.28
y = float(1.14)
print(type(gpa))

# complex type, this wont be used in this course, mostly used in electrical engineering
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built-in functions for numbers
print(abs(gpa))  # absolute value
print(abs(gpa * -1))  # will give 3.28 because abs function

print(round(gpa))  # round to nearest integer
# round to nearest decimal place that we specified, which is 1 here
print(round(gpa, 1))


# in this line we entered import math, upon saving it automatically moves up to the top right before our first line of code
# Python has a built-in module called math, which extends the list of mathematical functions.
# To use it, you must import the math module:
# import math
# When you have imported the math module, you can start using methods and constants of the module.

# this gives out the value of pi from the math module
print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))  # rounds down the gpa value
print(math.floor(gpa))  # rounds up the gpa value

# casting a string to a number
zipcode = "10001"

# the int() function turns the "10001" string into an integer
zip_value = int(zipcode)
print(type(zip_value))

# Error if you attemp to cast incorrect data
# zip_value = int("New York")
