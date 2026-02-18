import os, random, time

def play_typing_number_seq():
    os.system("clear")
    print("🔢 Typing Number Sequence Game")
    seq = [str(random.randint(0,9)) for _ in range(5)]
    print("Type this sequence: "," ".join(seq))
    start = time.time()
    user = input("Your input: ").split()
    end = time.time()
    if user==seq:
        print(f"✅ Correct! Time: {end-start:.2f}s")
    else:
        print("❌ Wrong sequence")
