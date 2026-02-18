import os

def play_sudoku():
    os.system("clear")
    print("🔢 Sudoku Game (Mini 4x4)")
    board=[[1,0,0,4],[0,0,2,0],[0,3,0,0],[2,0,0,1]]
    for row in board:
        print(row)
    print("Solve manually in your mind or paper!")
    input("Press Enter to return to menu...")
