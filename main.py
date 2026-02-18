import os
from guess_the_number import play_guess
from snake_game import play_snake
from quiz_game import play_quiz
from tictactoe import play_ttt
from rps_game import play_rps
from memory_game import play_memory
from simon_says import play_simon
from word_guess import play_word
from blackjack import play_blackjack
from rps_lizard_spock import play_lizard_spock
from sudoku_solver import play_sudoku
from color_guess import play_color
from catch_the_character import play_catch
from turtle_race import play_turtle
from typing_number_seq import play_typing
from number_puzzle import play_number_puzzle
from maze_runner import play_maze
from hangman import play_hangman
from emoji_catcher import play_emoji
from quick_type import play_quick
from reaction_timer import play_reaction
from word_scramble import play_scramble
from alien_shooter import play_alien
from falling_blocks import play_falling
from coin_collector import play_coin

def clear():
    os.system("clear")

def banner():
    print("""
╔═════════════════════════════════╗
║        GCS TERMINAL GAMES       ║
╠═════════════════════════════════╣
║ 1️⃣  Guess the Number           ║
║ 2️⃣  Snake Game                 ║
║ 3️⃣  Quiz Game                  ║
║ 4️⃣  Tic-Tac-Toe                ║
║ 5️⃣  Rock-Paper-Scissors        ║
║ 6️⃣  Memory Game                ║
║ 7️⃣  Simon Says                  ║
║ 8️⃣  Word Guess                  ║
║ 9️⃣  Blackjack                   ║
║ 🔟  RPS Lizard-Spock             ║
║ 11️⃣ Sudoku Solver               ║
║ 12️⃣ Color Guess                 ║
║ 13️⃣ Catch the Character         ║
║ 14️⃣ Turtle Race                 ║
║ 15️⃣ Typing Number Sequence      ║
║ 16️⃣ Number Puzzle               ║
║ 17️⃣ Maze Runner                 ║
║ 18️⃣ Hangman                     ║
║ 19️⃣ Emoji Catcher               ║
║ 20️⃣ Quick Type                  ║
║ 21️⃣ Reaction Timer              ║
║ 22️⃣ Word Scramble               ║
║ 23️⃣ Alien Shooter               ║
║ 24️⃣ Falling Blocks              ║
║ 25️⃣ Coin Collector              ║
║ 0️⃣  Exit                        ║
╚═════════════════════════════════╝
""")

def main():
    while True:
        clear()
        banner()
        choice = input("Choose a game: ")
        if choice == "1": play_guess()
        elif choice == "2": play_snake()
        elif choice == "3": play_quiz()
        elif choice == "4": play_ttt()
        elif choice == "5": play_rps()
        elif choice == "6": play_memory()
        elif choice == "7": play_simon()
        elif choice == "8": play_word()
        elif choice == "9": play_blackjack()
        elif choice == "10": play_lizard_spock()
        elif choice == "11": play_sudoku()
        elif choice == "12": play_color()
        elif choice == "13": play_catch()
        elif choice == "14": play_turtle()
        elif choice == "15": play_typing()
        elif choice == "16": play_number_puzzle()
        elif choice == "17": play_maze()
        elif choice == "18": play_hangman()
        elif choice == "19": play_emoji()
        elif choice == "20": play_quick()
        elif choice == "21": play_reaction()
        elif choice == "22": play_scramble()
        elif choice == "23": play_alien()
        elif choice == "24": play_falling()
        elif choice == "25": play_coin()
        elif choice == "0":
            print("Thanks for playing! 👾")
            break
        else:
            print("Invalid choice!")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
