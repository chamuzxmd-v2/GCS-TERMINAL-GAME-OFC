import os, random
from colorama import Fore, Style, init
init(autoreset=True)

def play_color_guess():
    os.system("clear")
    print("🎨 Color Guess Game")
    colors = [Fore.RED+"Red", Fore.GREEN+"Green", Fore.BLUE+"Blue", Fore.YELLOW+"Yellow"]
    real = random.choice(["Red","Green","Blue","Yellow"])
    print("Color to guess:", random.choice(colors))
    guess = input("Type the color name: ").capitalize()
    if guess==real:
        print("✅ Correct!")
    else:
        print(f"❌ Wrong! It was {real}")
