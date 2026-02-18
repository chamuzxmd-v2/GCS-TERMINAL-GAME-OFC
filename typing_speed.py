import os, time

def play_typing_speed():
    os.system("clear")
    print("⌨️ Typing Speed Test")
    text = "gcs terminal games are fun and challenging"
    print(f"Type this:\n{text}")
    input("Press Enter to start...")
    start = time.time()
    typed = input("Type here: ")
    end = time.time()
    speed = len(typed.split()) / ((end-start)/60)
    print(f"Your speed: {speed:.2f} words per minute")
    input("Press Enter to return to menu...")
