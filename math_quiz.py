import random, os

def play_math_quiz():
    os.system("clear")
    print("➗ Math Quiz Hard Mode")
    score = 0
    for _ in range(5):
        a = random.randint(1,50)
        b = random.randint(1,50)
        op = random.choice(["+","-","*"])
        answer = eval(f"{a}{op}{b}")
        user = int(input(f"{a} {op} {b} = "))
        if user == answer:
            print("✅ Correct")
            score += 1
        else:
            print(f"❌ Wrong, answer: {answer}")
    print(f"Score: {score}/5")
    input("Press Enter to return to menu...")
