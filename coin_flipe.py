import random, os

def play_coin():
    os.system("clear")
    print("🪙 Coin Flip Game")
    while True:
        user = input("Guess Heads or Tails (or exit): ").lower()
        if user=="exit":
            break
        comp = random.choice(["heads","tails"])
        print(f"Coin: {comp}")
        if user==comp:
            print("✅ You guessed it!")
        else:
            print("❌ Wrong guess!")
