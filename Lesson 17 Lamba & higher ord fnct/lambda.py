# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# syntax below
# lambda arguments : expression


from functools import reduce
def squared(num): return num * num
# lambda num : num * num this is how its written originally before autoformat


print(squared(2))


def addTwo(num): return num + 2
# lambda num : num + 2


print(addTwo(12))


def sum_total(a, b): return a + b
# lambda a, b : a + b


print(sum_total(10, 8))

#######################
# when lambdas are used


def funcBuilder(x):
    return lambda num: num + x


addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))  # x = 10, and 7 = num
print(addTwenty(7))

#######################
# higher order functions are defined as taking in  1 or more functions as arguments or returning a function. the fucbuilder above is an example.


numbers = [3, 7, 12, 18, 20, 21]

squared_nums = map(lambda num: num * num, numbers)
# map is a built in python function that recieves a function as the 1st argument.
# we can put in the numbers data collection too.
# the lambda function will square each value in the numbers list
print(list(squared_nums))

#######################
# another built in function: filter
# % returns the remainder of division. != is not equal to, which returns a true or false
# num / 2 get the remainder, then if its not equal to 0 then it would be odd which would return true
odd_nums = filter(lambda num: num % 2 != 0, numbers)
# filter returns the true conditions of being odd in the numbers list
print(list(odd_nums))

#######################
# functools is a built in module from the standard library that provides functions for working with higher order functions
# The reduce () function in Python is a built-in function that applies a given function to the elements of an iterable, reducing them to a single value.

numbers = [1, 2, 3, 4, 5, 1]

total = reduce(lambda acc, curr: acc + curr, numbers, 10)
# 2 ways to calculate the total sum of a list of numbers, with an initial value provided.
print(total)  # 26

print(sum(numbers, 10))  # 26


#####
names = ['Dave Gray', 'Sara Ito', 'John Jacob Jingleheimerschmidt']

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(char_count)

# # Explanation:
# The reduce function is used with a lambda function and an initial value of 0.
# The lambda function takes two parameters, acc (accumulator) and curr (current element from the list).
# For each name in the names list, the lambda function calculates the length of the name (len(curr)) and adds it to the accumulator (acc).
# The initial value of 0 ensures that the accumulator starts from zero.
# The final result is the total character count of all names in the list.
