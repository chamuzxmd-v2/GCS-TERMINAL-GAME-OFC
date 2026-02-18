import os, random, time

def play_turtle_race():
    os.system("clear")
    print("🐢 Turtle Race")
    turtles = {"A":0,"B":0,"C":0}
    finish = 20
    while max(turtles.values())<finish:
        for t in turtles:
            turtles[t]+=random.randint(0,2)
        print(" ".join([f"{k}:{v}" for k,v in turtles.items()]))
        time.sleep(0.5)
    winner = max(turtles,key=turtles.get)
    print(f"🎉 Turtle {winner} wins!")
