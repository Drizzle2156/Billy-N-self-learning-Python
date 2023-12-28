# #1 In Python, the %s formatting is used to format strings. It is a placeholder that
# indicates where a string should be inserted into another string.
# This formatting is often referred to as "string interpolation" or "string formatting."

name = "John"
age = 25

# Using %s formatting to insert string and integer into a string
message = "My name is %s, and I am %s years old." % (name, age)

print(message)

# In this example, %s is a placeholder for a string, and
# it is used twice in the string message. The values of the variables name and
# age are inserted into the string at the positions of the %s placeholders.

# In the resulting string, %s is replaced by the values of the corresponding variables.
# The output will be: My name is John, and I am 25 years old.

# You can use %s with various types of data, not just strings.
# Python will automatically convert the values to strings before inserting them into the string.


# #2 String.format method

# The str.format() method in Python is another way to perform string formatting.
# It provides a more flexible and powerful mechanism compared to the older % formatting.
# The str.format() method allows you to create strings by inserting values into placeholders within a string.

# Here's a basic example of how to use str.format():

# Using str.format() method to insert values into a string
message = "My name is {}, and I am {} years old.".format(name, age)

print(message)


# f strings, just use this now

message = f"My name is {name}, and I am {age} years old."

print(message)
# In this example, the f-string is created by prefixing the string literal with the letter 'f'.
# Inside the string, expressions enclosed in curly braces {} are evaluated at runtime and replaced with their values.
