import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


# we come back to add a while loop to the rps game, line 13 and 15
playagain = True

while playagain:
    # need to select all code below, press tab to add indentation for while loop
    # print("") replaced all 3 of these with \n
    playerchoice = input(
        "Enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

    player = int(playerchoice)

    if player < 1 or player > 3:
        sys.exit("You must enter 1, 2, or 3.")

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    # print("")
    print("\nYou chose " + str(RPS(player)).replace('RPS.', '') + ".")
    print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".\n")
    # print("")

    if player == 1 and computer == 3:
        print("🎉 You win!")
    elif player == 2 and computer == 1:
        print("🎉 You win!")
    elif player == 3 and computer == 2:
        print("🎉 You win!")
    elif player == computer:
        print("😲 Tie game!")
    else:
        print("🐍 Python wins!")
# everything below is new
    playagain = input("\nPlay again? \nY for Yes or \nQ to Quit \n\n")
# anything thats not a Y or y will quit the game
    if playagain.lower() == "y":
        continue
    else:
        print("🎉🙌")
        print("Thank you for playing!\n")
        playagain = False  # this ends the loop
# could also use a break to end loop


sys.exit("Bye! 👋")
