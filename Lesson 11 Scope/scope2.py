
name = "Dave"  # this in the global scope (available everywhere in this file)
count = 1

# function inside a function
# try to keep global scope as simple as possible


def another():  # parent function
    color = "blue"  # parent scope
    # count += 1 you can't modify global scope in local scope
    global count  # had to use global keyword to create a new variable of count
    count += 1
    print(count)

    def greeting(name):
        nonlocal color  # nonlocal keyword allows reuse of
        color = "red"
        print(color)
        print(name)

    greeting("Dave")


# remember to backspace next line to take it out of the ident from function creation
another()  # blue + Dave because the greeting function also prints #blue in addition to name
