#!/usr/bin/python3
""" This Module contain the main function that runs TIC-TAC-TOE Game
"""
from game_engine import play_game


def main():
    """The main function"""
    play_check = "1"
    while play_check == "1":
        print(
            "\t\t==================== LET'S PLAY = TIC-TAC-TOE GAME ======================\t\t\n\n"
        )
        play_game()
        play_check = input("Do you wish to continue? (1. Yes / 2. No): ")

    print("GAME ENDS!!!")


if __name__ == "__main__":
    main()