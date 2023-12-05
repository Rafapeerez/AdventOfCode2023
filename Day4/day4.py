def separateRows( lst ) :
    lst1 = []
    lst2= []
    for n in range(len(lst)):
        if n < 10:
            lst1.append(lst[n]) 
        elif n > 10:
            lst2.append(lst[n]) 
    results = set(lst1) & set(lst2)

    return results

sumTotal = 0

def sumPoints( results ) :
    sumPointCard = 0
    if len(results) != 0:
        global sumTotal
        for n in range(len(results)):
            if n == 0:
                sumPointCard = sumPointCard + 1
            else :
                sumPointCard = sumPointCard * 2
    sumTotal = sumTotal + sumPointCard

with open("Puzzle.txt", "r") as f:
    for line in f:
        lst = line.split()
        lst.remove(lst[0])
        lst.remove(lst[0])
        clean = lst[0].strip(':')
        lst[0] = clean
        sumPoints(separateRows(lst))
print(sumTotal)
