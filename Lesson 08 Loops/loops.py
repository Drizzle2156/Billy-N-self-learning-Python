# While loop
value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1


# while value <= 10:
#     value += 1
#     if value == 5: #Continue to the next iteration if i is 5:
#         continue
#     print(value)
# else: #With the else statement we can run a block of code once when the condition no longer is true:
#     print("Value is now = to " + str(value))

# For loop

names = ["Dave", "Sara", "John"]
# for x in names:
#     print(x)

# for x in "Mississippi":
#     print(x)

# for x in names:
#     if x == "Sara":
#         break  # break stops the loop
#     print(x)  # will print Dave and it stops there

# for x in names:
#     if x == "Sara":
#         continue
#     print(x)

# for x in range(4):
#     print(x)
# this goes from 0 to 3,


# for x in range(2,4):
#     print(x)
# this goes from 2 to 3


for x in range(0, 101, 5):
    print(x)
# this goes from 0 to 100, increments by 5
else:  # once range is done do the below
    print("Glad that\'s over!")


names = ["Dave", "Sara", "John"]
actions = ["codes", "eats", "sleeps"]

# nested for loop (loop inside a loop)
# the innter loop will be executed 1 time for each iteration of the outer loop
# name is outer loop, action is inner loop. Dave codes, Sara eats, etc)
# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")

for action in actions:
    for name in names:
        print(name + " " + action + ".")
# move on to rps2.py file
