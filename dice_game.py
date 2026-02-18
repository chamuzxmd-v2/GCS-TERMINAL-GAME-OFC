import random, os

def play_dice():
    os.system("clear")
    print("🎲 Dice Roller Game")
    while True:
        input("Press Enter to roll the dice (or type exit): ")
        print(f"🎲 You rolled: {random.randint(1,6)}")
        cont = input("Roll again? (y/n): ").lower()
        if cont != "y":
            break
