import sys
import random
from enum import Enum

# incorporating closures to rps game


def rps():  # new this is the outer enclosing function
    game_count = 0  # not using a global variable anymore, tab it, its in scope of rps function now
    player_wins = 0  # new
    python_wins = 0  # new

    def play_rps():  # nested function or closure
        nonlocal player_wins  # new
        nonlocal python_wins  # new

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input(
            "\nEnter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

        if playerchoice not in ["1", "2", "3"]:
            print("You must enter 1, 2, or 3.")
            return play_rps()

        player = int(playerchoice)

        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print("\nYou chose " + str(RPS(player)).replace('RPS.', '').title() + ".")
        print("Python chose " + str(RPS(computer)
                                    ).replace('RPS.', '').title() + ".\n")

        def decide_winner(player, computer):
            nonlocal player_wins  # new
            nonlocal python_wins  # new
            if player == 1 and computer == 3:
                player_wins += 1  # new
                return "🎉 You win!"
            elif player == 2 and computer == 1:
                player_wins += 1  # new
                return "🎉 You win!"
            elif player == 3 and computer == 2:
                player_wins += 1  # new
                return "🎉 You win!"
            elif player == computer:
                return "😲 Tie game!"
            else:
                python_wins += 1
                return "🐍 Python wins!"

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count  # global change it to nonlocal
        game_count += 1

        print("\nGame count: " + str(game_count))
        print("\nPlayer wins: " + str(player_wins))  # new
        print("\nPython wins: " + str(python_wins))  # new

        print("\nPlay again?")

        while True:
            playagain = input("\nY for Yes or \nQ to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_rps()
        else:
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            sys.exit("Bye! 👋")
    return play_rps


# Create closures below
play = rps()  # play_rps gets changed to rps because play_rps is no longer in global scope

# Call the closures
play()
