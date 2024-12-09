# Day 7
# Input = Combination of equations
# Each line is an equation
# Operators = "+" Add and "*" Multiply
# Evaluated left to right
# Out of all the combinations with operators, only true combinations remain
# Sum all correct items

import re

# Variables


# Read input
with open("./example.txt", "r") as file:
    input_data = file.readlines()

finalList = []


# Part 1
for comb in input_data:
    print("")
    print(comb)

    # Parse
    parsed = [int(x) for x in re.findall("(\d{1,9})", comb)]
    answer = parsed[0]
    equationNumbers = parsed[1:]
    print(f"Answer: {answer}")
    print(f"Equation: {equationNumbers}")

    # Test each possibility
    def allAdd(answer, equationNumbers):
        i = 0
        totalSum = 0
        for number in equationNumbers:
            totalSum += int(equationNumbers[i])
            i += 1
        print(f"Total Sum: {totalSum}")
        return totalSum

    def allMulti(answer, equationNumbers):
        totalMulti = int(equationNumbers[0])
        i = 1
        # totalMulti = list(map(lambda x: x[0] * x[1], zip(equationNumbers, equationNumbers[1:])))
        for number in equationNumbers[1:]:
            totalMulti = totalMulti * equationNumbers[i]
            i += 1
        print(f"Total Multi: {totalMulti}")
        return totalMulti

    def check_possible(answer, equationNumbers):
        # Add, then Multiply
        question = ""
        for i, value in enumerate(equationNumbers):
            if i % 2 == 0:
                if i == len(equationNumbers) - 1:
                    question = question + f"{value}"
                else:
                    question = question + f"{value}+"
            else:
                if i == len(equationNumbers) - 1:
                    question = question + f"{value}"
                else:
                    question = question + f"{value}*"
        
        print(question)
        print(f"{eval(question)}")
        if eval(question) == answer:
            print("Answer has been matched!")
            finalList.append(equationNumbers)
        
        # Multiply, then Add
        question = ""
        for i, value in enumerate(equationNumbers):
            if i % 2 == 0:
                if i == len(equationNumbers) - 1:
                    question = question + f"{value}"
                else:
                    question = question + f"{value}*"
            else:
                if i == len(equationNumbers) - 1:
                    question = question + f"{value}"
                else:
                    question = question + f"{value}+"
        
        print(question)
        print(f"{eval(question)}")
        if eval(question) == answer:
            print("Answer has been matched!")
            finalList.append(equationNumbers)
        
        

    # if allAdd(answer, equationNumbers) == int(answer):
    #     print(f"All numbers sum to answer!")
    # if allMulti(answer, equationNumbers) == int(answer):
    #     print(f"All numbers multi to answer!")
    check_possible(answer, equationNumbers)

print(finalList)