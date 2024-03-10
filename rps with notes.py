import sys
import random
from enum import Enum
# with the command line arguments we can personalize the rps game with f strings
import arcade

# from arcade import name
# from arcade import arcade


def rps_game(name='None'):  # originally I addded the name='PlayerOne'

    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():  # added nonlocal name
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

# enums are only used in line 38-40
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3
# enter f string and {name} for input, beginning of program in terminal
        playerchoice = input(
            f"\n{name}, please enter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

        if playerchoice not in ["1", "2", "3"]:
            # changed Player to f string {name}
            print(f"{name}, please enter 1, 2, or 3.")
            return play_rps()

        player = int(playerchoice)
        computerchoice = random.choice("123")
        computer = int(computerchoice)
# need to use str method here because RPS(player) returns an object and need to convert it to str. also added f string name to replace You
        print(f"\n{name}, chose {
              str(RPS(player)).replace('RPS.', '').title()}.")
        print(
            f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}.\n"
        )
# replaced return player_wins with return f"{name}, you win

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return f"🎉 {name}, you win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"🎉{name}, you win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"🎉{name}, you win!"
            elif player == computer:
                return "😲 Tie game!"
            else:
                python_wins += 1
                return f"🐍 Python wins!\nSorry, {name}..😭"

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        # removed str constructor, not needed here because f strings automatically converts variables inside {} to strings
        print(f"\nGame count: {game_count}")
        # replace player with f"{name}""
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nPython wins: {python_wins}")

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
            # arcade.ReadyGamer(name)
            sys.exit("Bye!")

    return play_rps  # we need to return the play function to capture the results


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized rps game experience."
    )

    parser.add_argument("-n", "--name", metavar="name", required=True,  help="The name of the person playing the game."
                        )

    args = parser.parse_args()

    # add args.name into rps to implement the command line argument
    rock_paper_scissors = rps_game(args.name)
    rock_paper_scissors()


# in order to run the program now, you have to first need to enter your name in the command line in terminal.
# python3 rps8.py -n "Dave"
# now for each game it has your entered name for win count.
