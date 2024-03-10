import sys
import random
from enum import Enum
# dont import the entire arcade, only the function to play arcade again when exiting


def rps_main(name='None'):
    game_count = 0
    player_wins = 0
    python_wins = 0
    print(f"This is the rps_main executing")

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins
        print(f"this is the play_rps executing")

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input(
            f"\n{name}, please enter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return play_rps()

        player = int(playerchoice)

        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print(f"\n{name}, you chose {
              str(RPS(player)).replace('RPS.', '').title()}.")
        print(
            f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}.\n"
        )

        def decide_winner(player, computer):
            print(f"this is decide winner executing")
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return f"🎉 {name}, you win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"🎉 {name}, you win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"🎉 {name}, you win!"
            elif player == computer:
                return "😲 Tie game!"
            else:
                python_wins += 1
                return f"🐍 Python wins!\nSorry, {name}..😢"

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nPython wins: {python_wins}")

        print(f"\nPlay again, {name}?")

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
            # import the main functions here to avoid a circular import error with rps, guess num and arcade
            # from arcade import arcade_main
            # arcade_main(name)
            from arcade import second_arcade
            second_arcade(name)

            # sys.exit(f"Bye {name}! 👋")

    return play_rps()  # THIS IS WHAT I NEEDED TO KNOW HOW TO FIX MY PROGRAM. THE DIFFERENCE BETWEEN NOT HAVING () AND HAVING IT. BECAUSE BEFORE THE PLAY RPS WAS NOT ACTUALLY WORKING IN THE ARCADE MODULE. ALSO INSERTING PRINT STATEMENTS WITHIN EACH FUNCTION HELPED ME NARROW DOWN WHATS WORKING AND NOT WORKING.


# this below allows it to be run directly without cmd line arguments, however when its imported to arcade the program automatically plays and skips the arcade function...
# ExecuteRps = rps_main()
# ExecuteRps()


def test():
    print("This is the rps file")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized RPS game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    rock_paper_scissors = rps_main(args.name)
    rock_paper_scissors()
