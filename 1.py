# Day 1
# Part 1
# Pair up smallest in list 1 with smallest in list 2
# Subtract (must be positive number)
# Add up all distances

import re
import time
from collections import Counter

# Sample
# list1 = [3, 4, 2, 1, 3, 3]
# list2 = [4, 3, 5, 3, 9, 3]

# Open text file
with open("1.txt", "r") as file:
    input_data = file.readlines()

list1 = []
list2 = []

# Read each line, parse with RE
for line in input_data:
    match1 = re.search("^\d{5}", line).group()
    list1.append(int(match1))
    match2 = re.search("\d{5}$", line).group()
    list2.append(int(match2))

list1 = sorted(list1)
list2 = sorted(list2)

finalList = []
x = 0
while x != len(list1):
    distance = list1[x] - list2[x]
    if distance < 0:
        distance = distance * -1
    finalList.append(distance)
    x += 1

print("Distances:")
print(finalList)

print("Sum of list:")
print(sum(finalList))

# Part 2
# Find out how many times a number appears on the left list
# Multiply it by how many times it appears in the right list
# Add to a finalList

list1 = []
list2 = []
finalList = []

# Read each line, parse with RE
for line in input_data:
    match1 = re.search("^\d{5}", line).group()
    list1.append(int(match1))
    match2 = re.search("\d{5}$", line).group()
    list2.append(int(match2))

# List1 needs to be unique numbers only
list1 = list(sorted(set(list1)))
counts = Counter(list2)

# Loop
for x in list1:
    instanceCount = counts[x]
    print(f"{x} appears {instanceCount} in list")
    # Multiply x by instanceCount
    sscore = x * instanceCount
    finalList.append(sscore)
    print(f"Sim Score: {sscore}")

print("Sum of list:")
print(sum(finalList))
