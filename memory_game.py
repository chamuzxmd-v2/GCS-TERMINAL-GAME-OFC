import random, time, os

def play_memory():
    os.system("clear")
    print("🧠 Memory Game")
    sequence = []
    score = 0
    while True:
        sequence.append(str(random.randint(0,9)))
        print("Remember this sequence:")
        print(" ".join(sequence))
        time.sleep(1 + len(sequence)/2)
        os.system("clear")
        user = input("Enter sequence separated by space: ").split()
        if user == sequence:
            print("Correct! ✅")
            score += 1
        else:
            print(f"Wrong ❌. Final Score: {score}")
            break
