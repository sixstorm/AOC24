# Day 3
# Computer memory (input) has been corrupted
# Instructions = "mul(x,y)"
# Example = mul(44, 46) means 44 * 46 = 2024
# There are chars to be ignored
# Find instances of mul(x,y), multiply them, then add all up

# Part 1

example = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
with open("./example.txt", "r") as file:
    example = file.readlines()

import re
import time

totalSum = 0

# Read input data from text file
with open("./3.txt", "r") as file:
    input_data = file.readlines()

def part1(input_data):

    for line in input_data:
        # Find all instances of mul(x,y)
        results = re.findall("(mul\(\d{1,3},\d{1,3}\))", line)

        # Multiply each one and add to totalSum
        lineSum = 0
        for r in results:
            numbers = re.findall("\d{1,3}", r)
            answer = int(numbers[0]) * int(numbers[1])
            lineSum += answer

        print("")
        print(f"Line: {line}")
        print(f"Line Sum: {lineSum}")

        totalSum += lineSum

    print(f"Final Sum: {totalSum}")

# Part 2

def part2(input_data):
    totalSum = 0
    breakout = []
    for line in input_data:
        # print(line)
        # Find all strings between "don't()...do()" or "don't()...$" and remove
        print(line)
        tempLine = re.sub("(don't\(\).*)do\(\)", "", line)
        tempLine = re.sub("(don't\(\).*)$", "", tempLine)
        print(tempLine)


        # tempLine = re.findall("(don't\(\).*)$", line)
        # for t in tempLine:
        #     print(t)
        # tempLine = re.sub("(don't\(\).*)do\(\)", "", line)
    #     print(tempLine)
    #     for t in tempLine:
        validInsts = re.findall("(mul\(\d{1,3},\d{1,3}\))", tempLine)
            # print(validInsts)
            
        for inst in validInsts:
            numbers = re.findall("\d{1,3}", inst)
            answer = int(numbers[0]) * int(numbers[1])
            totalSum += answer
    print(totalSum)

part2(input_data)