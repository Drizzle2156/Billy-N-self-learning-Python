person = "Dave"
coins = 3

print("\n" + person + " has " + str(coins) + " coins left.")
# there is a better way to format strings explained below

# %s method
message = "\n%s has %s coins left." % (person, coins)
print(message)

# string.format() method with 4 ways to use it

message = "\n{} has {} coins left.".format(person, coins)
print(message)

# putting in index numbers. coins is 0, and 1 is person,
message = "\n{1} has {0} coins left.".format(coins, person)
print(message)

# set the values of the parameters inside {}
message = "\n{person} has {coins} coins left.".format(
    coins=coins, person=person
)
print(message)


# create dictionary. ** pulls in values from player dictionary
player = {'person': 'Dave', 'coins': 3}

message = "\n{person} has {coins} coins left.".format(**player)
print(message)

###########
# f-strings, this is the method everyone should only use now to keep code at a minimum


message = f"\n{person} has {coins} coins left."
print(message)

# can do math inside {}
message = f"\n{person} has {2 * 5} coins left."
print(message)

# can use methods to edit strings inside {}
message = f"\n{person.lower()} has {2 * 5} coins left."
print(message)

# can put in dictionaries
message = f"\n{player['person']} has {2 * 5} coins left."
print(message)


##################
# You can pass formatting options

num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}\n")
# :.2f: This is the formatting specification. In this case : is the format specifier.
# .2f specifies the format for the floating-point number.
# It means that the floating-point number will be formatted with
# two digits after the decimal point. So 22.5067 becomes 22.50

# using for loop for f strings
for num in range(1, 11):
    print(f"2.25 times {num} is {2.25 * num:.2f}")


for num in range(1, 11):
    print(f"{num} divided by 4.52 is {num / 4.52:.2%}")


# can use all the string formats for f strings from
# https://www.w3schools.com/python/ref_string_format.asp
