# to run the arcade.py go into terminal and type in python3 arcade.py -n "insert any name here", enter
# requires command line arguments to enter name. Then you get a welcome message, and given choice of picking betwwen the 2 games or press x to exit arcade. In arcade i need to give ability to just loop through if i dont pick 1 or 2. then Need to give rps and guess games ability to come back to arcade.py when hitting Q.
# import the libraries in rps and guess number first
import sys
import guess_number
import rps

# need to figure out how to make the name global so that it wont reset to Gamer when switching between modules. Update on 1/11/2024. so apparently global variables only work in the file it was created, however when doing the import statement it already imports all the variables from that module..
# in order to transfer the name between modules, just do rps_main(name) and guessnumber_main(name). didnt need to do global or anything

# none is the default but gets replaced by the args.name


def arcade_main(name='None'):

    print(f"\n{name}, welcome to the Arcade! 🤖 ")
    GamerChoice = input(
        f"\nPlease choose a game:\n1 = Rock Paper Scissors\n2 = Guess My Number\n\nOr press 'x' to exit the Arcade\n")
# the data type of user inputs always returns a string
    if GamerChoice not in ["1", "2", "x"]:
        print(f"{name}, please enter 1, 2, or x")
        # NEEDED TO ADD IN name to the return arcade() SO THAT IT DOES NOT DEFAULT BACK TO NONE WHEN Entering SOMETHING OTHER THAN 1,2, OR X
        return arcade_main(name)

    # Gamer = int(GamerChoice) dont need to convert 1 or 2 into an integer

    def pick_game():  # inner function
        nonlocal name
        nonlocal GamerChoice

        if GamerChoice == "1":
            rps.test()
            rps.rps_main(name)

        elif GamerChoice == "2":
            guess_number.test2()
            guess_number.guessnumber_main(name)
        else:
            print(f"See you next time!\nBye {name}!")
            sys.exit()

    # adding () fixed the program of not being able to loop the act of acessing rps or guess game after inputting 1 or 2
    # removed () to get rid of nonetype error...
    # added () to pickgame  in order to be able to loop the arcade picking when coming back
    return pick_game()


# This one is the version that will play instead of when coming back to the arcade from the other modules. So that I can have a different welcome message
def second_arcade(name='None'):
    print(f"\n{name}, welcome back to the Arcade menu.")
    GamerChoice = input(
        f"\nPlease choose a game:\n1 = Rock Paper Scissors\n2 = Guess My Number\n\nOr press 'x' to exit the Arcade\n")
    if GamerChoice not in ["1", "2", "x"]:
        print(f"{name}, please enter 1, 2, or x")
        return second_arcade(name)

    def second_pick_game():
        nonlocal GamerChoice
        if GamerChoice == "1":
            rps.test()
            rps.rps_main(name)
        elif GamerChoice == "2":
            guess_number.test2()
            guess_number.guessnumber_main(name)
        else:
            print(f"See you next time!\nBye {name}!")
            sys.exit()
    return second_pick_game()
   # adding () to the return second_pick_game fixed the nonetype error


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Allows gamers to pick between 2 games"
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the Arcade."
    )

    args = parser.parse_args()

    ReadyGamer = arcade_main(args.name)
    ReadyGamer()
