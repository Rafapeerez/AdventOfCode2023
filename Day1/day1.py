import re

sumTotal = 0
numberRegex = r'\d'

with open("Puzzle.txt", "r") as f:
    for line in f : 
        numbersPosition = re.findall(numberRegex, line)

        if (len(numbersPosition) == 1) :
            sumLine = numbersPosition[0] + numbersPosition[0]
        else :
            sumLine = numbersPosition[0] 
            numbersPosition.reverse()
            sumLine = sumLine + numbersPosition[0]

        sumTotal = sumTotal + int(sumLine)

print(sumTotal)
f.close()
