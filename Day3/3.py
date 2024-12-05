# Day 3
# Computer memory (input) has been corrupted
# Instructions = "mul(x,y)"
# Example = mul(44, 46) means 44 * 46 = 2024
# There are chars to be ignored
# Find instances of mul(x,y), multiply them, then add all up

# Part 1

example = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

import re
import time

totalSum = 0

# Read input data from text file
with open("./3.txt", "r") as file:
    input_data = file.readlines()

for line in input_data:
    # Find all instances of mul(x,y)
    results = re.findall("(mul\(\d{1,3},\d{1,3}\))", line)

    # Multiply each one and add to totalSum
    lineSum = 0
    for r in results:
        numbers = re.findall("\d{1,3}", r)
        answer = int(numbers[0]) * int(numbers[1])
        print(f"{answer=}")
        lineSum += answer

    print("")
    print(f"Line: {line}")
    print(f"Line Sum: {lineSum}")

    totalSum += lineSum

print(f"Final Sum: {totalSum}")

# Part 2

# 2 new Instructions: do() an don't()
print("")
print("PART 2")
totalSum2 = 0
for line in input_data:
    print("")
    reg4 = "don't\(\)(.*)do\(\)|don't\(\)(.*)$"

    newLine = re.sub(reg4, "", line)
    print(newLine)

    for nGroup in re.findall("mul\((\d{1,3},\d{1,3})\)", newLine):
        print(f"{nGroup=}")
        numbers = re.findall("\d{1,3}", nGroup)
        totalSum2 += int(numbers[0]) * int(numbers[1])
#    searchResults = (
#        re.findall(reg1, line) + re.findall(reg2, line) + re.findall(reg3, line)
#    )
#    print(searchResults)
#
#    for item in searchResults:
#        numbers = re.findall("mul\((\d{1,3},\d{1,3})\)", item)
#        print(f"{numbers=}")
#        for n in numbers:
#            totalSum2 += int(n.split(",")[0]) * int(n.split(",")[1])

print(totalSum2)
