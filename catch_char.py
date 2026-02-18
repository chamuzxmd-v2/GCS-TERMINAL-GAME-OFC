import os, random, time

def play_catch_char():
    os.system("clear")
    print("👾 Catch the Character Game")
    for i in range(5):
        target = random.choice(["a","b","c","d","e"])
        print(f"Catch: {target}")
        user = input("Type character: ").lower()
        if user==target:
            print("✅ Caught!")
        else:
            print("❌ Missed")
        time.sleep(0.5)
