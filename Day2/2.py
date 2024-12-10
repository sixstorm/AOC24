# Day 2
# Data from the reactor
# Unusual data is the input
# One report per line
# Levels separated by spaces
# Which reports are safe?
# Safe has 2 conditions - AND, not OR
# 1. Levels are either all increasing or all decreasing
# 2. Any two adjacent levels differ by at least one and at most three

import time

with open("./example.txt", "r") as file:
    example = file.readlines()

with open("./2.txt", "r") as file:
    pInput = file.readlines()

safeReports = []
unsafeReports = []


def check_1(inputList):
    if inputList == sorted(inputList) or inputList == sorted(inputList, reverse=True):
        return True
    else:
        return False


def check_2(inputList):
    x = 0
    result = False

    while x < len(inputList) - 1:
        difference = abs(inputList[x] - inputList[x + 1])
        print(f"{difference=}")
        if difference > 0 and difference <= 3:
            result = True
        else:
            result = False
            x = len(inputList)
            break
        x += 1

    return result

def part1(input):
    for line in input:
        inputList = [int(x) for x in line.rstrip().split(" ")]

        # Check 1
        check1 = check_1(inputList)
        print(check1)

        # Check 2
        check2 = check_2(inputList)
        print(check2)

        # Final Check
        if check1 and check2:
            safeReports.append(line)
        else:
            unsafeReports.append(line)

    print(len(safeReports))

def part2(unsafeReports):
    print("Part 2")
    print(f"{unsafeReports}")
    for line in unsafeReports:
        inputList = [int(x) for x in line.rstrip().split(" ")]

        for i, value in enumerate(inputList):
            print(f"{i}-{value}")
            tempList = inputList[:i]+inputList[i+1:]
            print(f"{tempList=}")

            # Check 1
            check1 = check_1(tempList)
            print(f"{check1=}")

            # Check 2
            check2 = check_2(tempList)
            print(f"{check2=}")

            if check1 and check2:
                safeReports.append(line)
                break


                time.sleep(1)
    print(f"Safe Reports: {len(safeReports)}")
    print(f"{safeReports}")




part1(pInput)
part2(unsafeReports)

# # Read in 1 line at a time
# for line in input_data:
#     # Convert string into list of ints
#     line = list(line.rstrip().split(" "))
#     line = [int(i) for i in line]
#     print(line)

#     check1 = check_1(line)
#     print(f"Check1: {check1}")
#     check2 = check_2(line)
#     print(f"Check2: {check2}")

#     if check1 and check2:
#         safeReports.append(line)
#     else:
#         unsafeReports.append(line)

# print("")
# print(f"Safe Reports: {len(safeReports)}")
# print(safeReports)
# print(f"Unsafe Reports: {len(unsafeReports)}")
# print(unsafeReports)


# # Part 2
# # If one level can be removed, does it make it safe?
# print("")
# print("Part 2")
# print("")

# for line in unsafeReports:
#     print(f"Line: {line}")

#     # Loop through each possibility
#     x = 0
#     for level in line:
#         print("")
#         print(f"X: {x}")
#         # Create a tempLine where index x is removed
#         # tempLine = [i for i in line if i != line[x]]
#         tempLine = line
#         tempLine.remove(level)
#         print(f"Removing {level}")
#         print(f"TempLine: {tempLine}")

#         # Check 1
#         check1 = check_1(tempLine)
#         print(f"Check 1 Results: {check1}")

#         # Check 2
#         check2 = check_2(tempLine)
#         print(f"Check 2 Results: {check2}")

#         if check1 and check2:
#             unsafeReports = [l for l in unsafeReports if l != line]
#             print("Unsafe")
#             print(unsafeReports)
#             safeReports.append(line)
#             print("Safe")
#             print(safeReports)
#             print("Breaking on 2")
#             break
#         x += 1

# print("")
# print(f"Safe Reports: {len(safeReports)}")
# print(safeReports)
# print(f"Unsafe Reports: {len(unsafeReports)}")
# print(unsafeReports)
