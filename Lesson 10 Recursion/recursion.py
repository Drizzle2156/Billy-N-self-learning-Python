# recursive functions are functions that calls itself
# Using an if statement without an else is possible, by using the return statements.
# the return num + 1 ends the code block, and spits out a value
def add_one(num):
    # base case
    if (num >= 9):  # the recursion stops when num = 9 or greater
        return num + 1  # the function ends with the return

# recursive base
    total = num + 1
    print(total)  # this only prints up to 9

    return add_one(total)  # the recursive call


# here we use the recursive function
mynewtotal = add_one(0)
print(mynewtotal)

# for num = 0 it works like this. 0 is < 9 so it goes to recursive base.
#  the 0 goes to total = 0 + 1, it gets printed as 1 and
# then 1 gets returned and called again as add_one(total), where it goes through
# the same process again. This repeats until the base case is true, the final
# value ends as 9 , gets returned as 9 + 1 and code block is ended
