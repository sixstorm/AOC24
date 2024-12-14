# Day 10
# Fill in missing hiking trails for a scorched topographic map
# 0 (lowest) and 9 (highest)
#
# Example:
# 0123
# 1234
# 8765
# 9876
#
# Trail means an even, uphill slope (0-9, step of 1)
# Only up, down, left, and right movements, no diagonals.
# Trailheads - Trails that can split into two or more trails
# Each trail is a score of 1

import time
totalScore = 0

with open("./example.txt", "r") as file:
    example = file.read().splitlines()

def look_around2(input, x, y, z):
    coords = [(x-1, y), {x+1, y}, {x, y-1}, {x, y+1}]
    z += 1
    for coord in coords:
        i, j = coord
        print(input[i][j])
        if input[i][j] == z:
            print(f"{i}:{j}:{z}")
            look_around2(input, x, y, z)

def look_around(input, x, y, z):
    global totalScore
    # Look at surrounding numbers
    print(f"Initiating look_around with {x}:{y}:{z}")
    sList = []
    # Up
    # If up is possible
    if (x-1) >=0:
        print("Pass up 1")
        # If coordinate value is z+1, recurse
        if input[x-1][y] == str(z+1):
            print("Pass up 2")
            print(f"Found {z+1} at {x-1}:{y}")
            if input[x-1][y] == "9":
                print("Up is 9")
                totalScore += 1
        else:
            look_around(input, x-1, y, z+1)

    # Down
    # If down is possible
    if (x+1) < len(example):
        print("Pass down 1")
        # If coordinate value is z+1, recurse
        if input[x+1][y] == str(z+1):
            print("Pass down 2")
            print(f"Found {z+1} at {x+1}:{y}")
            if input[x-1][y] == "9":
                print("Down is 9")
                totalScore += 1
            else:
                look_around(input, x+1, y, z+1)

    # Left
    # If left is possible
    if (y-1) >= 0:
        print("Pass left 1")
        # If coordinate value is z+1, recurse
        if input[x][y-1] == str(z+1):
            print("Pass left 2")
            print(f"Found {z+1} at {x}:{y-1}")
            if input[x-1][y] == "9":
                print("Left is 9")
                totalScore += 1
        else:
            look_around(input, x, y-1, z+1)

    # Right
    # If right is possible
    if (y+1) < len(line):
        print("Pass right 1")
        # If coordinate value is z+1, recurse
        if input[x][y+1] == str(z+1):
            print("Pass right 2")
            print(f"Found {z+1} at {x}:{y+1}")
            if input[x-1][y] == "9":
                print("Right is 9")
                totalScore += 1
        else:
            look_around(input, x, y+1, z+1)

    return sList


for line in example:
    print(line)
    x = 0
    z = 0
    for y, number in enumerate(line):
        if number == str(z):
            look_around2(example, x, y, z)

            # print(f"{x}")
            # print(f"{y}")
            # print(f"{example[x][y]=}")
            # print(sList)

            # for coord in sList:
            #     x, y, value = coord
            #     if value == str(z+1):
            #         print(f"{z+1} found!")
    x += 1

print(f"{totalScore=}")