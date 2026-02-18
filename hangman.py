import os, random

def play_hangman():
    os.system("clear")
    print("🪢 Hangman Game")
    words = ["python","terminal","gcs","programming","developer"]
    word = random.choice(words)
    guessed = ["_"]*len(word)
    attempts = 6

    while attempts > 0 and "_" in guessed:
        print("Word: "," ".join(guessed))
        print(f"Attempts left: {attempts}")
        letter = input("Guess a letter: ").lower()
        if letter in word:
            for i, l in enumerate(word):
                if l == letter:
                    guessed[i] = letter
        else:
            print("Wrong guess! ❌")
            attempts -= 1
    if "_" not in guessed:
        print(f"🎉 You won! The word was {word}")
    else:
        print(f"💀 You lost! The word was {word}")
    input("Press Enter to return to menu...")
