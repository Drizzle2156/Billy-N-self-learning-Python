# Dictionaries: are used to store data values that are in key pairs
# the right sides are the values, doesnt have to be a string
# the left sides are the keys
band = {
    "vocals": "Plant",
    "guitar": "Page"
}

# the 2nd way to create a dictionary
band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))  # dictionaries are the 'dict' class
print(len(band))  # gives out number of pairs in the dictionary

# 2 ways Access dictionary items

# print the "vocals" value of the dictionary, which is plant
print(band["vocals"])
print(band.get("guitar"))  # same thing here, page

# list all keys
print(band.keys())

# list all values
print(band.values())

# list of key/value pairs as tuples (unchangable lists)
# done using items() method for dictionaries
print(band.items())
# 2:22:05

# verify a key exists
print("guitar" in band)
print("triangle" in band)

# change values in a dictionary
# vocals: Plant pair -> changed to vocals: Coverdale
band["vocals"] = "Coverdale"
# this one adds a new pair, bass: JPJ
band.update({"bass": "JPJ"})

print(band)
# 2:24:58 left off

# remove items. bass and JPJ pair are removed
# the pop() method removes and returns an item from a dictionary based on its key
# in this case the key is bass from the dictionary
print(band.pop("bass"))
print(band)

# add new pair
band["drums"] = "Bonham"
print(band)

# popitem() removes the last pair in dictionary and returns it as a tuple
# here we are printing the last pair we just removed
print(band.popitem())  # tuple
print(band)

# Delete and clear
band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)  # outputs {}

del band2

# this is not the way to copy dictionaries
# band2 = band  # creates a reference
# print("Bad copy!")
# print(band2)
# print(band)

# band2["drums"] = "Dave"
# print(band)

# the correct way to make a dictionary copy
band2 = band.copy()
band2["drums"] = "Dave"
print("Good copy!")
print(band)
print(band2)

# or use the dict() constructor function
band3 = dict(band)
print("Good copy!")
print(band3)

# Nested dictionaries are dictionaries that contain dictionaries
member1 = {
    "name": "Plant",
    "instrument": "vocals"
}

member2 = {
    "name": "Page",
    "instrument": "guitar"
}
# this is the nested dictionary which contains member1, member2 dictionaries
band = {
    "member1": member1,
    "member2": member2,
}
print(band)
# access items/values in nested dictionaries, use name of outer, inner, then key
print(band["member1"]["name"])
# 2:35:46

# Sets, the 4th data collection type after lists, tuples, dictionaries
# sets = {}
# lists = ()
# dictionaries = {
#  "key":"value",
#  "key2":"value2"
# }
nums = {1, 2, 3, 4}

nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))  # sets are objects with the data type set
print(len(nums))


# Sets can't have 2 items with the same value, it will be ignroed
nums = {1, 2, 2, 3}
print(nums)

# True is a dupe of 1, False is a dupe of 0
# True = 1 and False = 0
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# check if a value is in a set, True or False
print(2 in nums)

# but you cannot refer to an element in the set with an index position (list) or a key (dictionary)

# Add a new element to a set
nums.add(8)
print(nums)

# Add elements from 1 set to another set
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

# you can use update method with lists, tuples, dictionaries too

# merge 2 sets to create a new set
one = {1, 2, 3}
two = {5, 6, 7}

mynewset = one.union(two)
print(mynewset)

# Keep only the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)

# Keep everything except the duplicates
one = {1, 2, 3}
two = {2, 3, 4}
one.symmetric_difference_update(two)
print(one)
