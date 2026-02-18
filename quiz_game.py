def play_quiz():
    import os
    os.system("clear")
    print("📝 Quiz Game")
    questions = {
        "What is 2+2? ": "4",
        "Capital of Sri Lanka? ": "Colombo",
        "Python is a ____? ": "Programming"
    }
    score = 0
    for q, ans in questions.items():
        user = input(q)
        if user.strip().lower() == ans.lower():
            print("Correct! ✅")
            score += 1
        else:
            print(f"Wrong ❌. Answer: {ans}")
    print(f"Your Score: {score}/{len(questions)}")
    input("Press Enter to return to menu...")
