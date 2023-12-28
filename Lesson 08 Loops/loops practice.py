

# "For loop" iterates over the list 'fruits' and prints each fruit
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# "While loop" executes a set of statements as long as a condition is true
i = 1
while i < 6:
    print(i)
    i += 1

# the break statement can stop the loop before it loops through all the items
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print(x)
#     if x == "banana":
#         break


# nested loops, you can add more loops inside it too
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

# So, the key difference is in the order in which the names and actions are combined.
# The first loop combines each name with all actions before moving to the next name,
# while the second loop combines each action with all names before moving to the next action.


names = ["Dave", "Sara", "John"]
actions = ["codes", "eats", "sleeps"]
# This loop iterates through each name in the names list and, for each name, iterates through each action in the actions list.
for name in names:
    for action in actions:
        print(name + " " + action + ".")

print("    ")
print("    ")
# It first iterates through each action in the actions list and, for each action, iterates through each name in the names list.
for action in actions:
    for name in names:
        print(name + " " + action + ".")
