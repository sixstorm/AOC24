# Day 4
# Word search
# Horizontal, vertical, diagnal, written backwards, or overlapping

import time
import re

# 980 = Too low

# Part 1
# How many times does XMAS appear with the rules above?

with open("./4.txt", "r") as file:
    input_data = file.readlines()

input = []
totalCount = 0

for line in input_data:
    tempLine = [i for i in line if i != "\n"]
    input.append(tempLine)

print(input)

# x = 0
# y = 2
# print(f"{x=}, {y=}")
# print(input[x][y])


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


def check_ahead(line):
    global totalCount
    straight_occur = re.findall("(?=(XMAS))", line)
    print(f"Found {len(straight_occur)} in {line}")
    if straight_occur:
        totalCount += 1


def check_backwards(line):
    global totalCount
    backwards = re.findall("(?=(SAMX))", line)
    print(f"Found {len(backwards)} backwards in {line}")
    if backwards:
        totalCount += 1


x = 0
y = 0

# Straight through and backwards
# for line in input_data:
# check_ahead(line)
# check_backwards(line)
# print(f"{totalCount=}")

for line in input:
    print("")
    print(line)

    for single in line:
        # print(single)
        if single == "X":
            print("")
            # print(f"{x},{y} is X")
            check_grid2(line, input, x, y)
        y += 1
    x += 1
    y = 0

print(f"{totalCount=}")

# for y in input[x]:
#    print(f"{y=}")
#    check_grid(input, x, y)
#    time.sleep(2)
#    x += 1
