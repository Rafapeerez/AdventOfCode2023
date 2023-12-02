import re

sumIds = 0

def checkList(lst):
    for x in range(len(lst)):
        if lst[x] in ('red', 'red,', 'red;'):
            if x + 1 < len(lst) and int(lst[x+1]) > 12:
                return False
        elif lst[x] in ('green', 'green,', 'green;'):
            if x + 1 < len(lst) and int(lst[x+1]) > 13:
                return False
        elif lst[x] in ('blue', 'blue,', 'blue;'):
            if x + 1 < len(lst) and int(lst[x+1]) > 14:
                return False
    return True

with open("Puzzle.txt", "r") as f:
    for line in f:
        x = line.split()
        if checkList(x[::-1]):
            id = x[1].strip(':')
            sumIds = sumIds + int(id)

print(sumIds)
f.close()   