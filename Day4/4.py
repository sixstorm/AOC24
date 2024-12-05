# Day 4
# Word search
# Horizontal, vertical, diagnal, written backwards, or overlapping

import time
import re

# Part 1
# How many times does XMAS appear with the rules above?

with open("./4.txt", "r") as file:
    input_data = file.readlines()

input = []
totalCount = 0
part2Count = 0

for line in input_data:
    tempLine = [i for i in line if i != "\n"]
    input.append(tempLine)

print(input)


def check_grid2(line, input, x, y):
    global totalCount

    # Check up and left
    if x >= 3 and y >= 3:
        try:
            if (
                (input[x - 1][y - 1] == "M")
                and (input[x - 2][y - 2] == "A")
                and (input[x - 3][y - 3] == "S")
            ):
                print(f"Found upper left for {x},{y}")
                totalCount += 1
        except IndexError:
            print("Grid error")

    # Check up and right
    if x >= 3 and y <= (len(line) - 3):
        try:
            if (
                (input[x - 1][y + 1] == "M")
                and (input[x - 2][y + 2] == "A")
                and (input[x - 3][y + 3] == "S")
            ):
                print(f"Found upper right for {x},{y}")
                totalCount += 1
        except IndexError:
            print("Grid error")

    # Check down and left
    if x <= (len(line) - 3) and y >= 3:
        try:
            if (
                (input[x + 1][y - 1] == "M")
                and (input[x + 2][y - 2] == "A")
                and (input[x + 3][y - 3] == "S")
            ):
                print(f"Found lower left for {x},{y}")
                totalCount += 1
        except IndexError:
            print("Grid error")

    # Check down and right
    if x <= (len(input) - 3) and y <= (len(line) - 3):
        try:
            if (
                (input[x + 1][y + 1] == "M")
                and (input[x + 2][y + 2] == "A")
                and (input[x + 3][y + 3] == "S")
            ):
                print(f"Found lower right for {x},{y}")
                totalCount += 1
        except IndexError:
            print("Grid error")

    # Check straight up
    if x >= 3:
        try:
            if (
                (input[x - 1][y] == "M")
                and (input[x - 2][y] == "A")
                and (input[x - 3][y] == "S")
            ):
                print(f"Found straight up for {x},{y}")
                totalCount += 1
        except IndexError:
            print("Grid error")

    # Check straight down
    if x <= (len(input) - 3):
        try:
            if (
                (input[x + 1][y] == "M")
                and (input[x + 2][y] == "A")
                and (input[x + 3][y] == "S")
            ):
                print(f"Found straight down for {x},{y}")
                totalCount += 1
        except IndexError:
            print("Grid error")

    # Straight across
    if y <= (len(line) - 3):
        try:
            if (
                (input[x][y + 1] == "M")
                and (input[x][y + 2] == "A")
                and (input[x][y + 3] == "S")
            ):
                print(f"Found straight across for {x},{y}")
                totalCount += 1
        except IndexError:
            print("Grid error")

    # Backwards
    if y >= 3:
        try:
            if (
                (input[x][y - 1] == "M")
                and (input[x][y - 2] == "A")
                and (input[x][y - 3] == "S")
            ):
                print(f"Found backwards for {x},{y}")
                totalCount += 1
        except IndexError:
            print("Grid error")


def part2(input, x, y):
    # Focused on the "A", look diagnally for M and S.
    # X must be 1 down from top or 1 up from bottom
    # Y must be 1 from the beginning or end of input
    global part2Count

    if (x >= 1) and (y >= 1):
        print("Attemping to check A")
        try:
            if (input[x - 1][y - 1] == "M" and input[x - 1][y + 1] == "S") and (
                input[x + 1][y - 1] == "M" and input[x + 1][y + 1] == "S"
            ):
                print(f"Found crossing at {x},{y}")
                part2Count += 1
        except IndexError:
            print("Grid error")

        try:

            if (input[x - 1][y - 1] == "S" and input[x - 1][y + 1] == "S") and (
                input[x + 1][y - 1] == "M" and input[x + 1][y + 1] == "M"
            ):
                print(f"Found crossing at {x},{y}")
                part2Count += 1
        except IndexError:
            print("Grid error")

        try:
            if (input[x - 1][y - 1] == "M" and input[x - 1][y + 1] == "M") and (
                input[x + 1][y - 1] == "S" and input[x + 1][y + 1] == "S"
            ):
                print(f"Found crossing at {x},{y}")
                part2Count += 1
        except IndexError:
            print("Grid error")

        try:
            if (input[x - 1][y - 1] == "S" and input[x - 1][y + 1] == "M") and (
                input[x + 1][y - 1] == "S" and input[x + 1][y + 1] == "M"
            ):
                print(f"Found crossing at {x},{y}")
                part2Count += 1
        except IndexError:
            print("Grid error")


x = 0
y = 0

for line in input:
    print("")
    print(line)

    for single in line:
        #        if single == "X":
        #            print("")
        #            check_grid2(line, input, x, y)
        if single == "A":
            print("")
            print(f"A at {x},{y}")
            part2(input, x, y)
        y += 1
    x += 1
    y = 0

print(f"{totalCount=}")
print(f"{part2Count=}")
