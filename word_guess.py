import os, random

def play_word_guess():
    os.system("clear")
    print("🔤 Word Guess Game")
    words = ["python","terminal","gcs","developer","game"]
    word = random.choice(words)
    hidden = ["_"]*len(word)
    while "_" in hidden:
        print(" ".join(hidden))
        guess = input("Guess a letter: ").lower()
        if guess in word:
            for i,l in enumerate(word):
                if l==guess:
                    hidden[i]=guess
        else:
            print("Wrong guess ❌")
    print(f"🎉 You guessed the word: {word}")
