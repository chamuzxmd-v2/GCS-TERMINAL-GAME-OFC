import os, random, time

def play_simon():
    os.system("clear")
    print("🎵 Simon Says Game")
    colors = ["Red","Green","Blue","Yellow"]
    sequence = []
    while True:
        sequence.append(random.choice(colors))
        print("Sequence:")
        print(" ".join(sequence))
        time.sleep(1 + len(sequence)/2)
        os.system("clear")
        user = input("Repeat sequence (space-separated) or 'exit': ").split()
        if user==["exit"]:
            break
        if user != sequence:
            print("❌ Wrong sequence! Game Over.")
            break
        print("✅ Correct! Next round...")
