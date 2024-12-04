# Day 3
# Computer memory (input) has been corrupted
# Instructions = "mul(x,y)"
# Example = mul(44, 46) means 44 * 46 = 2024
# There are chars to be ignored
# Find instances of mul(x,y), multiply them, then add all up

# Part 1

example = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

import re

# Find all instances of mul(x,y)
# results = re.findall("(mul\(\d{1,3},\d{1,3}\))", example)
# print(example)

totalSum = 0

# Read input data from text file
with open("./example.txt", "r") as file:
    input_data = file.readlines()

for line in input_data:
    # Find all instances of mul(x,y)
    results = re.findall("(mul\(\d{1,3},\d{1,3}\))", line)

    # Multiply each one and add to totalSum
    lineSum = 0
    for r in results:
        print(f"{r=}")
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
for line in input_data:
    print("")

    # Regex - All matches up to 'do'
    # reg1 = "^.*(mul\(\d{1,3},\d{1,3}\))do"
    reg1 = "^(.*)do\(\)"

    # Regex - All matches between 'do' and 'don't'
    # reg2 = "do(.*(mul\(\d{1,3},\d{1,3}\)).*)don't()"
    reg2 = "do\(\)(.*)don't\(\)"

    searchResults = re.findall(reg2, line)
    print(searchResults)
