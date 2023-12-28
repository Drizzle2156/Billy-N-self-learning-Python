# Closure is a function having access to the scope of its parent
# function after the parent function has returned.

def parent_function(person, coins):  # parent aka outer function
    # coins = 3

    def play_game():  # inner function
        nonlocal coins
        coins -= 1  # -= adds a - to the 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left.")
        else:
            print("\n" + person + " is out of coins.")

    return play_game  # complete parent function


tommy = parent_function("Tommy", 3)
jenny = parent_function("Jenny", 5)

tommy()
tommy()

jenny()

tommy()
