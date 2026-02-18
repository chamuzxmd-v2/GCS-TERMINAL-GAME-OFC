import random
import os

def play_guess():
    os.system("clear")
    print("🎯 Welcome to Guess the Number!")
    number = random.randint(1,50)
    attempts = 0
    while True:
        try:
            guess = int(input("Enter your guess (1-50): "))
            attempts += 1
            if guess < number:
                print("Too low! 📉")
            elif guess > number:
                print("Too high! 📈")
            else:
                print(f"🎉 Congrats! You guessed in {attempts} attempts!")
                break
        except ValueError:
            print("Please enter a number.")
    input("Press Enter to return to menu...")
