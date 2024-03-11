import os  # os modules gives functions to interact with the operating system, such as the file system
# read w3schools -> Python File Open
# r = Read
# a = Append
# w = Write
# x = Create

# Read - error if it doesn't exist

f = open("names.txt", "r")
# print(f.read())
# print(f.read(4))

print(f.readline())
print(f.readline())

for line in f:
    print(line)
f.close()  # should always close a file after opening it

# to avoid an error use a try block

try:
    f = open("name_list.txt")  # also try names.txt to avoid the error message
    print(f.read())
except:
    print("The file you want to read doesn't exist")
finally:
    f.close()

# "a" is Append, which creates the file if it doesn't exist
f = open("names.txt", "a")
# this will write Neil whereever you left your cursor at in the names.txt file
f.write("Neil")
f.close()

f = open("names.txt")
print(f.read())
f.close()

# "w" is write, opens a file for writing, creates the file if it doesnt exist, (overwrite)
f = open("context.txt", "w")
f.write("I delete all of the context")
f.close()

f = open("context.txt")
print(f.read())
f.close()

# 2 ways to create a new file

# Opens a file for writing, creates the file if it does not exist
f = open("names_list.txt", "w")
f.close()

# Creates the specified file, but returns an error if the file exists

if not os.path.exists("dave.txt"):
    f = open("dave.txt", "x")
    f.close()

# Delete a file
# avoid an error if it doesn't exist
if os.path.exists("dave.txt"):
    os.remove("dave.txt")
else:
    print("The file you wish to delete does not exist")

with open("more_names.txt") as f:
    content = f.read()

with open("names.txt", "w") as f:
    f.write(content)
