import os

def play_maze():
    os.system("clear")
    print("🌀 Maze Game")
    maze = [
        ["#","#","#","#","#","#"],
        ["#"," "," "," ","E","#"],
        ["#"," ","#"," "," ","#"],
        ["#","S","#"," "," ","#"],
        ["#","#","#","#","#","#"]
    ]
    pos = [3,1] # Start S
    while True:
        for row in maze:
            print("".join(row))
        move = input("Move (W/A/S/D): ").upper()
        maze[pos[0]][pos[1]]=" "
        if move=="W": pos[0]-=1
        elif move=="S": pos[0]+=1
        elif move=="A": pos[1]-=1
        elif move=="D": pos[1]+=1
        if maze[pos[0]][pos[1]]=="#":
            print("Hit wall! ❌")
            break
        elif maze[pos[0]][pos[1]]=="E":
            print("🎉 You escaped the maze!")
            break
        maze[pos[0]][pos[1]]="S"
