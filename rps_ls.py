import os, random

def play_rps_ls():
    os.system("clear")
    print("✊ Rock-Paper-Scissors-Lizard-Spock")
    choices = ["rock","paper","scissors","lizard","spock"]
    wins = {"rock":["scissors","lizard"], "paper":["rock","spock"],
            "scissors":["paper","lizard"], "lizard":["spock","paper"],
            "spock":["scissors","rock"]}
    while True:
        user = input("Enter choice or exit: ").lower()
        if user=="exit": break
        if user not in choices: continue
        comp = random.choice(choices)
        print(f"Computer chose {comp}")
        if user==comp:
            print("Draw! 🤝")
        elif comp in wins[user]:
            print("🎉 You Win!")
        else:
            print("❌ You Lose!")
