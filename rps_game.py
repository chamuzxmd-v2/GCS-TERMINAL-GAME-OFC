import random

def play_rps():
    import os
    os.system("clear")
    print("✊ Rock-Paper-Scissors Game ✋")
    choices = ["rock","paper","scissors"]
    while True:
        user = input("Enter rock/paper/scissors or exit: ").lower()
        if user=="exit":
            break
        if user not in choices:
            print("Invalid choice!")
            continue
        comp = random.choice(choices)
        print(f"Computer chose {comp}")
        if user==comp:
            print("Draw!")
        elif (user=="rock" and comp=="scissors") or (user=="paper" and comp=="rock") or (user=="scissors" and comp=="paper"):
            print("You Win! 🎉")
        else:
            print("You Lose! ❌")
