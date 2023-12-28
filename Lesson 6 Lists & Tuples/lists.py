users = ['Dave', 'John', 'Sara']  # strings list

data = ['Dave', 42, True]  # can also use integers and boolean data

emptylist = []  # lists can also be empty

# to check if something is inside a list
print("Dave" in users)  # this will give a true or false if its in a list
# outputs the 1st item in users list. if you put 3 or above it will give an index error
print(users[0])
print(data[2])  # output True
print(users[-1])  # -1 gives the last value of the list
# counting from -1 gives the next value to the left and so forth in list
print(users[-2])  # -1 = sara, -2 = john

# this gives the position value of Sara in the users list
print(users.index('Sara'))

print(users[0:2])  # prints out the range excluding the position 2
# left off at 1:50:37

print(users[1:])  # prints out from the start all to the end of list
print(users[-3:-1])  # -3 = dave, excludes the value of -1
print(users[:])  # whole range of the 3 strings
print(len(data))  # length function counts the list specified
users.append('Elsa')  # to add more items to list, append method
print(users)

users += ['Jason']  # can add lists together and individual items
print(users)

# extend method adds list elements to add of current list
users.extend(['Robert', 'Jimmy'])
print(users)

# users.extend(data)  can also add an entire list
# print(users)
# everything above only adds to end of list

users.insert(0, 'Bob')  # specifies a spot in list, inserts string there
print(users)
# left off at 1:55

# brackets to insert more than 1 value at the 2nd spot. 2:2 begins and ends at spot 2
users[2:2] = ['Eddie', 'Alex']
print(users)

# this replaces Dave, and Eddie with the 2 strings
users[1:3] = ['Robert', 'JpJ']
print(users)

users.remove('Bob')  # removes Bob from the list
print(users)

print(users.pop())
print(users)

del users[0]  # deletes the 0 position in the users list
print(users)

# del data
data.clear()  # this will clear out all elements inthe list
print(data)

users[1:2] = ['dave']
users.sort()  # sorts lists alphabetically. lower case comes after upper
# list.sort() sorts numbers in a list from least to greatest by default
print(users)

# str.lower converts all charachters in a string to lowercase
users.sort(key=str.lower)
# key parameter is a sort function that allows modifications of default sorting behavior
# putting it all together, everything is sorted without considering the case of letters
print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)

# sorts the nums list in descending order using the sort() method
# nums.sort(reverse=True)
# print(nums)

# the sorted()  function creates a sorted version of the list without modifying the original list
print(sorted(nums, reverse=True))
print(nums)

# here are 3 ways to create a copy of a list
numscopy = nums.copy()  # copy() method
mynums = list(nums)  # list() function creates a list object
mycopy = nums[:]  # list slicing

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))  # type() function used to get the type of the object

mylist = list([1, "Neil", True])
print(mylist)

# Tuples are unchangable, and similar to lists but they are considered tuple objects not list
# 2 ways to make tuples,
# tuple() function. items inside it form the tuple
# (item 1, item2, item etc,) makes a tuple. whereas [] makes a list
mytuple = tuple(('Dave', 42, True))
anothertuple = (1, 4, 2, 8, 2, 2)
print(mytuple)
print(type(mytuple))
print(type(anothertuple))

# you can convert tuples to lists using list() function.
newlist = list(mytuple)
# now that mytuple became a list, you can modify it
newlist.append('Neil')  # append() function adds string to end of list
# you can convert lists to tuples using tuple() function
newtuple = tuple(newlist)
print(newtuple)

# tuple unpacking using the (*) to assign elements to the variables one, hey and two as a list
(one, *two, hey) = anothertuple
# In this example, one is assigned the value 1,
# two is assigned a list [4, 2, 8, 2] containing the elements between one and hey,
# and hey is assigned the value 2 (the 3rd 2). The use of the starred expression allows you to capture multiple elements into a list when unpacking a tuple or a list.
print(one)
print(two)
print(hey)

# tuples and lists have access to different methods
print(anothertuple.count(2))
