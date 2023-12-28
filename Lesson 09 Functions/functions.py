# functions are created using def keyword. the name needs to be all lower case and underscores
def hello_world():
    print("Hello World!")


# to use (otherwise known as call) a function, put the function name followed by ()
hello_world()

# parameters are variables used in the declaration of a function
# num1 and num2 are parameters of the sum function

# def sum(num1, num2):
# print(num1 + num2)

# arguments are specified after function name, inside parentheses
# You can add as many arguments as you want, just separate them with a comma.
# here we call the sum function using arguments
# sum(2, 3)  # 2 and 3 are arguments passed to the sum function. 2 will replace num1 and 3 will replace num2
# sum(1, 7)
# sum(100, 3)


# we can use if statements in functions to give a different outcome
# return allows
def sum(num1, num2):
    if (type(num1) is not int or type(num2) is not int):
        return  # early return
    return num1 + num2


# sum function
total = sum(1, 3)  # if you put a non integer value such as "a" I get none
# if its empty I get 0
print(total)


# start with * if i dont know how many will be inside
def multiple_items(*args):
    print(args)
    print(type(args))


# why this is a tuple (ask ChatGPT) check google doc #1 note
multiple_items("Dave", "John", "Sara")


# kwargs = keywords arguments
# check google doc #2 note
def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


mult_named_items(first="Dave", last="Gray")
