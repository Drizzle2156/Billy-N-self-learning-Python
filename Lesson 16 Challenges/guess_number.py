Challenge #1, Guess number game which is using the knowledge from rps game and applying it to a new problem
# Create a new game using knowledge from rps
# The following are Command line arguments in terminal
# python3 guess_number.py -n "Charly", enter
# outputs -> Charly, guess which number I'm thinking of... 1, 2, or 3.
# user inputs 1 2 or 3 in terminal and enter
# outputs the picture in google doc notes

import sys  # for interacting with python interpreter and system environment. such as command line arguments, sys.exit() to exit the script, and sys.version to findout
import random
from enum import Enum

class numbers(Enum):
    computer_choice1 = 1
    computer_choice2 = 2
    computer_choice3 = 3
