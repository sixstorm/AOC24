# Day 6
# ^ = Guard position
# ^ = Up
# < = Left
# V = Down
# > = Right
# # = Obstruction
# 
# Instructions:  Take a step forward unless obstruction.  If obstruction, turn right 90 degrees.
# Predict the path of the guard and count each position that he will walk in.

import time

# Variables

# Input
with open("./example.txt") as file:
    input_data = file.readlines()

# Create 2D Array
array_2d = [list(line.strip()) for line in input_data]
print(array_2d)


# Part 1
guardMoves = ["^", "<", ">", "V"]
swapX = []

def findGuard():
    global array_2d
    x = 0
    y = 0
    while x < len(array_2d):
        while y < len(list(array_2d[x])):
            print(f"{x},{y}")
            print(f"{array_2d[x][y]}")
            if array_2d[x][y] in guardMoves:
                print(f"Found guard at {x},{y}")
                return (x, y, array_2d[x][y])
            y += 1
        x += 1
        y = 0

def findUp(x, y):
    global array_2d, guardMove
    # Record positions until obstruction found
    offmap = False
    obFound = False
    array_2d[x][y] = "X"
    
    while not obFound:
        x -= 1
        if array_2d[x - 1][y] == ".":
            print(f"Replacing X at {x},{y}")
            array_2d[x][y] = "X"
        else:
            print(f"Guard stopped at {x},{y}")
            array_2d[x][y] = "X"
            print("Turning right")
            obFound = True
            for line in array_2d:
                print(line)

    guardMove = ">"


# Start
# Find position of guard at start
x, y, guardMove = findGuard()
print(f"{x=}")
print(f"{y=}")
print(f"{guardMove=}")



match guardMove:
    case "^":
        findUp(x, y)
    case ">":
        findRight(x, y)