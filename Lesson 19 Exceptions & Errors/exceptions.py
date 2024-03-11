# The code first defines a variable x and assigns it the value 2. It then tries to print the result of dividing x by 1. Since there are no errors, the else block is executed, and the code prints "No errors!".
# if x is undefined the name error occurs, or if its 0 division you get the other result.

# created our own custom exception
class JustNotCoolError(Exception):
    pass


x = 2
try:
    raise JustNotCoolError("This just isn't cool, man")
    # print(x / 0)
    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed.")  # built in error
    # raise Exception("I'm a custom exception!")
except NameError:
    print('NameError means something is probably undefined.')
except ZeroDivisionError:
    print('Please do not divide by zero')
except Exception as error:
    print(error)
else:  # else only happens if theres no errors
    print('No errors!')
finally:  # this part will always execute regardless of errors or not
    print("I'm going to print with or without an error.")


# need at least 1 except for try
