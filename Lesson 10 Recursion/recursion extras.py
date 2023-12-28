# in math n! = n * (n-1)!


def factorial(n):
    # Base case. This is the condition under which the function stops calling itself and returns a result directly.
    # It prevents the function from calling itself indefinitely, avoiding infinite recursion.
    if n == 0 or n == 1:
        return 1
    # Recursive case
    # This is where the function calls itself with a modified version of the input or with a different set of parameters.
    # Each recursive call should ideally reduce the problem toward the base case.
    else:
        return n * factorial(n - 1)


# Example usage
result = factorial(5)  # 5! = 5 * (5-1)! = 5 * 4 * 3 * 2 * 1 = 120
# for (n-1)! it counts from 5 down to 2. when n becomes 1 the base case applies
print(result)  # Output: 120

# Remember: The return statement in Python is used to exit a function and return a value.
# The value that is returned can then be used by the caller of the function.


# example from recursion file with no return statement for recursive call
# check note #1 google doc for explanation
def add_one(num):
    if (num >= 9):
        # If num is greater than or equal to 9, the function exits here.
        return num + 1

    total = num + 1
    print(total)

    add_one(total)  # This recursive call doesn't have a return statement.


mynewtotal = add_one(0)
print(mynewtotal)
