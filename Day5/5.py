# Day 5
# Safety protocols must be in a specific order
#
# Page Ordering Rules
# Example: 47|53
# If update includes page 47 and 53, then 47 must be printed before 53
#
# Updates
# Example: 75,47,61,53,29
# Page 75 must be printed before 47 (75|45), 75 before 61 (75|61), etc
#
# Middle page
# If order is correct, you must find the middle page and add to sum
# 75,47,61,53,29 - 61 is the middle page
#

import re
import time

with open("./example.txt", "r") as file:
    input_data = file.readlines()

# Variables
correctUpdates = []
incorrectUpdates = []
middleNumbers = []


def part1():
    totalSum = 0
    # Separate Rules from Updates
    pors = [i.rstrip() for i in input_data if "|" in i]
    updates = [i.rstrip() for i in input_data if "," in i]

    print(pors)

    for update in updates:
        correct = True
        # Iterate through each number, checking if it exists in pors list
        pages = update.rstrip().split(",")
        print(pages)

        pagesLength = len(pages)
        print(f"Update has {pagesLength} pages")

        # Start 1 ahead to make it work
        index = 1
        for page in pages:
            for p in pages[index:]:
                rule = f"{page}|{p}"
                if rule in pors:
                    print(f"{rule} was found in PORS")
                else:
                    correct = False
                    print(f"{rule} was NOT found in PORS")

            index += 1
        if correct == True:
            correctUpdates.append(update)
            middleNumbers.append(pages[len(pages) // 2])
            totalSum += int(pages[len(pages) // 2])

    print(correctUpdates)

    print("")
    print("Middle Numbers:")
    print(middleNumbers)
    print(f"{totalSum=}")


def part2():
    # Separate Rules from Updates
    pors = [i.rstrip() for i in input_data if "|" in i]
    updates = [i.rstrip() for i in input_data if "," in i]

    for update in updates:
        correct = True
        pages = update.rstrip().split(",")
        index = 1
        for page in pages:
            for p in pages[index:]:
                rule = f"{page}|{p}"
                if rule not in pors:
                    correct = False
            index += 1
        if correct == True:
            continue
        else:
            # Go through each number
            correct = False
            i1 = 0
            i2 = 1

            while not correct:
                while i2 < len(update):
                    rule = f"{update[i1]}|{update[i2]}"
                    if rule in pors:
                        print(f"{rule} has been found in PORS")
                    else:
                        print(
                            f"{rule} is not in PORS; swapping {update[i2]} with {update[i1]}"
                        )
                        update[i1], update[i2] = update[i2], update[i1]
                        print(update)
                        time.sleep(2)
                        break
                    i1 += 1
                    i2 += 1
                index += 1

def part3():
    # Separate Rules from Updates
    pors = [i.rstrip() for i in input_data if "|" in i]
    updates = [i.rstrip() for i in input_data if "," in i]

    for update in updates:
        print(update)
        updateSplit = update.split(",")
        print(updateSplit)

        # Print pairs
        pairs = [updateSplit[i:i+2] for i in range(0, len(updateSplit), 1)]
        pairs.remove(pairs[-1])
        print(pairs)

        for pair in pairs:
            if f"{pair[0]}|{pair[1]}" not in pors:
                print(f"{pair[0]}|{pair[1]}")
                

        # for page in updateSplit:
            # if page != updateSplit[-1]:
                # pair = f"{page}|{updateSplit[updateSplit.index(page) + 1]}"
                # if pair in pors:
                #     print(f"Found {pair} in PORS")
                # else:
                #     print(f"{pair} NOT found in PORS")
                #     updateSplit[updateSplit.index[page]], updateSplit[updateSplit.index(page) + 1] = updateSplit[updateSplit.index(page) + 1], updateSplit[updateSplit.index[page]]
                #     print(f"UPDATE: {updateSplit}")


# part1()
# part2()
part3()