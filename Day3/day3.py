#After many hours trying this challenge I have copied it from https://github.com/Futarimiti/advent-of-code2023/blob/main/3-gear-rations/main.py 


import math as m, re

board = list(open('Puzzle.txt')) #<--- Convert text into list of lists, each line is a list 
chars = {(r, c): [] for r in range(140) for c in range(140)
                    if board[r][c] not in '01234566789.'}   #<---(row, column) of each special caracter

for r, row in enumerate(board):
    for n in re.finditer(r'\d+', row): #<-- search each number
        edge = {(r, c) for r in (r-1, r, r+1)
                        for c in range(n.start()-1, n.end()+1)}    
        """ <--- It creates a set of index around the find number. Iterates over adjacent rows (r-1, r, r+1) 
        and columns covering the range from the starting position to the end of the found number. """   

        for o in edge & chars.keys(): #<--- Iterates over the intersection between the edge set and the keys (chars.keys()) of the chars dictionary.
            chars[o].append(int(n.group())) #<--- For each index already present in chars, it adds the number found to the associated list in the chars dictionary. 

print(  sum(sum(p)    for p in chars.values()),)