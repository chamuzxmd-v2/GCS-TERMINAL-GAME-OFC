import os, random

def play_number_puzzle():
    os.system("clear")
    print("🔢 15 Puzzle Game")
    puzzle = list(range(1,16))+[0]
    random.shuffle(puzzle)

    def print_puzzle():
        for i in range(0,16,4):
            print(" ".join([str(x).rjust(2) if x!=0 else "  " for x in puzzle]))
    
    while True:
        print_puzzle()
        move = input("Move tile number (or 'exit'): ")
        if move.lower() == "exit":
            break
        if not move.isdigit(): continue
        move = int(move)
        if move in puzzle:
            idx = puzzle.index(move)
            zero_idx = puzzle.index(0)
            # Swap if adjacent
            if abs(idx - zero_idx) in [1,4]:
                puzzle[idx], puzzle[zero_idx] = puzzle[zero_idx], puzzle[idx]
        if puzzle == list(range(1,16))+[0]:
            print("🎉 Puzzle Solved!")
            break
    input("Press Enter to return to menu...")
