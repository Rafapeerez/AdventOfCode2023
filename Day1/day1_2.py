import re

sumTotal = 0
numberRegex = r'\d'
cont=0

def convertToNumber( line ):
    x = line.replace('zero', '0o')
    x = x.replace('one', 'o1e')
    x = x.replace('two', 't2o')
    x = x.replace('three', 't3e')
    x = x.replace('four', '4')
    x = x.replace('five', '5e')
    x = x.replace('six', '6')
    x = x.replace('seven', '7n')
    x = x.replace('eight', 'e8t')
    return x.replace('nine', 'n9e') 


with open("Puzzle.txt", "r") as f:
    for line in f : 
        numbersPosition = re.findall(numberRegex, convertToNumber(line))
        if (len(numbersPosition) == 1) :
            sumLine = numbersPosition[0] + numbersPosition[0]
        else :
            sumLine = numbersPosition[0] 
            numbersPosition.reverse()
            sumLine = sumLine + numbersPosition[0]
        cont = cont +1

        sumTotal = sumTotal + int(sumLine)

print(sumTotal) 
f.close()