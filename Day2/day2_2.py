import re

multMinCubes = 0
redPerGame = []
greenPerGame = []
bluePerGame = []

def checkList(lst):
    redPerGame.clear(), greenPerGame.clear(), bluePerGame.clear()
    for x in range(len(lst)):
        if lst[x] in ('red', 'red,', 'red;'):
            redPerGame.append(int(lst[x+1])) #<--- we have to insert it as an int to sort the list well
        elif lst[x] in ('green', 'green,', 'green;'):
            greenPerGame.append(int(lst[x+1]))
        elif lst[x] in ('blue', 'blue,', 'blue;'):
            bluePerGame.append(int(lst[x+1]))

def maxOfList( lst ):
    lst.sort()
    lst.reverse()
    return lst[0] 

with open("Puzzle.txt", "r") as f:
    for line in f:
        x = line.split()
        checkList(x[::-1])

        minRed = maxOfList(redPerGame)
        minGreen = maxOfList(greenPerGame)
        minBlue = maxOfList(bluePerGame)
        multMinCubes = multMinCubes + (minRed * minGreen * minBlue) 

print(multMinCubes) 
f.close()   