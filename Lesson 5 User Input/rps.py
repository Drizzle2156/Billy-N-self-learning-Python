# rock paper scissors
# you can move the terminal location by view, panel position, and we pick right
# here we introduce the input function, which allows user input
# value = input("Please enter a value") # in the terminal you can type anything after value, and pressing enter will print it out

# here we add a new line \n (this is an escape character we learned about in past lesson)
# value = input("Please enter a value:\n")
# print(value)
import sys  # the system library provides access to variables, functions to interact with the interpreter. we are using it to exit the python program for code block line 19

import random # random module from python standard library to use for the computer choice
from enum import Enum #Enums are a set of symbolic names bound to unique values

class RPS(Enum):
    ROCK = 1 #all caps for constant variables
    PAPER = 2
    SCISSORS = 3
# checking    
# print(RPS(2)) is RPS.PAPER
# print(RPS.ROCK) is RPS.ROCK
# print(RPS['ROCK']) is RPS.ROCK
# print(RPS.ROCK.value) is 1
# sys.exit() exits the program right here

print("")
playerchoice = input(
    "Enter ... \n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n")
# A Python program is constructed from code blocks. A block is a piece of Python program text that is executed as a unit. The following are blocks: a module, a function body, and a class definition. line 15 and 16 is an example
# if 1 > 2:
#     print("do something")

player = int(playerchoice)  # convert  playerchoice to the integer data type

if player < 1 or player > 3:
    # print("You must enter 1, 2, or 3.") the problem with the print function is that the program will still run. we will add sys.exit to show the message and exit the program
    sys.exit("You must enter 1, 2, or 3.")

# this will randomly pick between 1,2,3 string
computerchoice = random.choice("123")

computer = int(computerchoice)  # convert variable into an integer

# at end of lesson, we replace playerchoice with str(RPS(player)).replace("RPS.", '') and computer choice with same but with computer instead of player.
print("")  # I WAS STUCK HERE ->> str(RPS(player)) is casting to a string, pass in RPS, and player value. it would output You chose RPS.PAPER for example which is strange for a user. We add the .replace string method. check txt file for better explanation
print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")
print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".")
print("")

# at this point it doesnt tell us who wins so we add line 40-49 below

#rememember that == is the equality operator to compare the values of the 2 operands, returning a boolean value of true or false
if player == 1 and computer == 3:
        print("🎉 You win!")
elif player == 2 and computer == 1: #elif is else if. its used when the first if statement isnt true but want to check another condition
        print("🎉 You win!")
elif player == 3 and computer == 1: #addition elif is used if the previous conditions above were not true
        print("🎉 You win!")
elif player == computer:
        print("😮 Tie game!")
else:
        print("🐍 Python wins!")

#we can add emojis to strings by keyboard shortcut fn/globe + e or edit, drop down box to emoji & symbols

#introduce python enums 