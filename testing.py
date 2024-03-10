# #Explanation:

# if __name__ == "__main__":: This is a common Python idiom that checks whether the script is being run as the main program (not imported as a module). The code within this block will be executed only when the script is run directly.

# parser = argparse.ArgumentParser(description="Allows gamers to pick between 2 games"): Creates an ArgumentParser object named parser with a description. This object will handle the parsing of command-line arguments.

# parser.add_argument(...):

# Adds a command-line argument for the player's name using the add_argument method. The argument can be specified using either -n or --name.
# metavar="name": Specifies the name to be used in the help message for the argument.
# required=True: Indicates that the argument is mandatory.
# help="The name of the person playing the Arcade.": Provides a help message for the argument.
# args = parser.parse_args(): Parses the command-line arguments using the ArgumentParser object, and stores the result in the args variable. The args object will contain the values of the parsed arguments.

# name = args.name: Extracts the value of the 'name' argument from the parsed arguments and assigns it to the variable name.

# ReadyGamer = arcade(name): Calls the arcade function (presumably defined elsewhere in the code) with the player's name and assigns the result to the variable ReadyGamer. Note that I removed args. from args.name because name is already extracted from args.

# ReadyGamer(): Calls the ReadyGamer function. This is presumably the main function that executes the Arcade game logic.

# In summary, this script uses the argparse module to handle command-line arguments, specifically expecting a player's name. It then calls the arcade function with the provided name and executes the game logic within the ReadyGamer function.
import rps

rps.rps()

# import argparse

# if __name__ == "__main__":

#     parser = argparse.ArgumentParser(
#         description="Allows gamers to pick between 2 games"
#     )

#     parser.add_argument(
#         "-n", "--name", metavar="name",
#         required=True, help="The name of the person playing the Arcade."
#     )

#     args = parser.parse_args()

#     name = args.name


# print(name)

# Now, in order to make name global i need to write ' global name ' right below     args = parser.parse_args()
