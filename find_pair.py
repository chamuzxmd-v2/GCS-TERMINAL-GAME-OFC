import random, os

def play_pair():
    os.system("clear")
    print("🃏 Find the Pair Game")
    cards = list("AABBCCDD")
    random.shuffle(cards)
    hidden = ["*"]*len(cards)

    while "*" in hidden:
        print(" ".join(hidden))
        try:
            i = int(input("Pick first card (0-7): "))
            j = int(input("Pick second card (0-7): "))
            if cards[i]==cards[j] and i!=j:
                print("✅ Match!")
                hidden[i]=hidden[j]=cards[i]
            else:
                print("❌ Not a match")
        except:
            print("Invalid input")
    print("🎉 You found all pairs!")
    input("Press Enter to return to menu...")
