
# A variable is only available from inside the region its created.
name = "Dave"  # this in the global scope (available everywhere in this file)


def greeting(name):  # variables created inside function belongs to the local scope of that function
    color = "blue"  # local scope
    print(color)
    print(name)


greeting("John")  # plug in string John into the greeting function
# print(color) can't use color outside of the local scope

# global and local scopes can be used in future functions


def another():
    greeting("Dave")


# remember to backspace next line to take it out of the ident from function creation
another()  # blue + Dave because the greeting function also prints blue in addition to name


# Function inside Function
# variable x is not available outside myfunc() but is available for any function within it


def myfunc():  # outer/parent scope
    x = 300

    def myinnerfunc():  # inner function
        print(x)
    myinnerfunc()


myfunc()


# check scope2 to continue video from around 3:47:00
