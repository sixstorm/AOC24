# Day 9
# Disk Map - Input
# Number represent alternating between file, then free space
# 0 = No free space
# Each file has an ID before they are rearranged, starting with 0
# Numbers are the ID and "." are free space

# Disk map '12345' is represented as "0..111....22222"

# Elf wants to move files to the left most place
# 0..111....22222
# 02.111....2222.
# 022111....222..
# 0221112...22...
# 02211122..2....
# 022111222......

import time

# example = "2333133121414131402"
# exampleMappedOut = "00...111...2...333.44.5555.6666.777.888899"
# Should be "00...111...2...333.44.5555.6666.777.888899"

with open("./Day9/9.txt", "r") as file:
    example = file.readlines()

print(example)
time.sleep(2)

# Part 1
# Map out
def map_out(input):
    diskMap = ""
    id = 0
    try:
        for file, space in zip(input[::2], input[1::2]):
            print(f"{file=} {space=}")
            diskMap += f"{str(id) * int(file)}{'.' * int(space)}"
            id += 1
        if len(input) % 2 != 0:
            print(f"This is the last: {str(id) * int(input[-1])}")
            diskMap += f"{str(id) * int(input[-1])}"
        print(f"{diskMap}")

        # if diskMap == exampleMappedOut:
        #     print("CORRECT")
        return diskMap
    except IndexError:
        None

def free_space(diskMap):
    diskMap = list(diskMap)
    y = -1

    for i, item in enumerate(diskMap):
        if all(x == diskMap[i] for x in diskMap[i:]):
            break
        if item == ".":
            print(f"{diskMap[i]}|{i} with {diskMap[y]}|{y} ")
            diskMap[i] = diskMap[y]
            diskMap[y] = "."
            while diskMap[y] == ".":
                print(y)
                y += -1
    return diskMap

def calc_checksum(diskMap):
    totalSum = 0
    for i, value in enumerate(diskMap):
        if value != ".":
            totalSum += i * int(value)
    return totalSum


diskMap = map_out(example[0])
diskMap = free_space(diskMap)
totalSum = calc_checksum(diskMap)
print(totalSum)