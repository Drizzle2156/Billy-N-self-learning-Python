# Guess Number game how it works
# Player picks 1,2, or 3. Computer then randomly picks 1,2,3
# If the computer ends up picking the same number as player, the player wins, but if not then the player loses.

import sys  # for interacting with python interpreter and system environment. such as command line arguments, sys.exit() to exit the script, and sys.version to findout
import random
# from enum import Enum

# import arcade


def guessnumber(name='None'):  # outer function
    game_count = 0
    player_wins = 0
    # percent = (value/total value)*100
    # apparently i cant define % right here because its currently at 0, maybe do it during game result
    # player_win_percent = (player_wins/game_count)*100
    # final_percent = "{:.2f}%".format(player_win_percent)

    def play_guessnumber():  # inner function. make sure all code below are tabbed to right to keep it in here
        nonlocal name
        nonlocal game_count
        nonlocal player_wins

# review enumerations in chapter 5. I dont think i really need to use enums in this program compared to the rock paper scissors game.
        # class ABC(Enum):
        #     CHOICE_A = 1
        #     CHOICE_B = 2
        #     CHOICE_C = 3

        playerchoice = input(
            f"\n{name}, guess which number I'm thinking of... 1, 2, or 3.\n\n")

        if playerchoice not in ["1", "2", "3"]:
            print(f"\n{name}, please enter 1, 2, or 3.")
            return play_guessnumber()  # this will loop the function to bring it back to beginning

        # converts chosen number into integer, we call this integer player now. We do this because initially 1,2,3 is a string
        player = int(playerchoice)
        # computer picks a random number
        computer_choice = random.choice("123")

        computer = int(computer_choice)  # convert number string to integer

        # to add variable into string use {}. In the RPS program we NEED TO USE ENUMS HERE, but i wont here
        print(f"\n{name}, you chose {player}.")

        print(f"\nI was thinking about the number {computer}.")

    # use a function if then else statement to pick the winner between.
    # Use nonlocal to make the variable refer to the scope just outside of it, in order to not create a new variable under the same name inside of that scope

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal game_count
            if player == computer:
                player_wins += 1

                return f"🎉 {name}, you win!"

            else:
                return f"Sorry {name}. Better luck next time. 😓"

        game_result = decide_winner(player, computer)
        game_count += 1
# I kept getting a 0 division error if I got 0 wins, causing the program to fail. It was fixed when I added this if else conditional statement
# so right now its not calculating my win percentage correctly. I got 1 win out of 2 games, it output 100% still
# i fixed it by moving the game_count +=1 from below print(game_result) to right above.
        if player_wins == 0:
            player_win_percent = 0

        else:
            player_win_percent = (player_wins/game_count * 100)

        final_percent = "{:.2f}%".format(player_win_percent)

        print(game_result)

        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nYour winning percentage: {final_percent}")
        print(f"Play again, {name}?")

        while True:
            playagain = input("\nY for Yes or \nQ to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            # this here will loop the game, results save from the return below and then game_count will increment again
            return play_guessnumber()
        else:
            print("\n🎉🎉🎉🎉")
            print(f"Thank you for playing!\n")
            sys.exit(f"Bye {name}! 👋")
            # return to arcade by getting rid of sys.exit, also get rid of import sys
            # print(f"{name}, welcome back to the Arcade menu.\n")

            # arcade.arcade()

    return play_guessnumber  # capture the results. need to review closure


second_game = guessnumber()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing guess # game."
    )

    args = parser.parse_args()

    second_game = guessnumber(args.name)
    second_game()
