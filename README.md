# AdventOfCode2023

## DAY 1
### First challenge
The objetive of this challenge is to combine the first digit and the last digit oof each line of the Puzzle.txt
to form a single two-digit number. For exaple:    
- 9dlvndqbddghpxc                             ----> 99   
- rtkrbtthree8sixfoureight6                   ----> 86   
- fdxrqmfxdkstpmcj7lmphgsmqqnmjrtwo3tcbc      ----> 73   
- onetjcsmgk57nvmkvcvkdtqtsksgpchsfsjzkkmb    ----> 57   
- TOTAL   ----> 315   

### Second challenge
The objective continue being the same, but now we have to consider the digits and when numbers are expressed with text.
For example:  
- two1nine            ----> 29  
- eightwothree        ----> 83   
- abcone2threexyz     ----> 13  
- xtwone3four         ----> 24  
- 4nineeightseven2    ----> 42  
- zoneight234         ----> 14  
- 7pqrstsixteen       ----> 76  
- TOTAL   ----> 281  

## DAY 2
### First challenge
The objective is know about what games' IDs are "available" and then add them. An ID is "available" when theirs red, green and blue cubes
don't exceed 12, 13 and 14 respectively in each "match". For example:  
- Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green                          ---->  POSSIBLE  
- Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue                ---->  POSSIBLE  
- Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red        ---->  IMPOSSIBLE  
- Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red        ---->  IMPOSSIBLE  
- Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green                          ---->  POSSIBLE  
- TOTAL   ---->  1 + 2 + 5 = 8  

### Second challenge
The objective changes in this challenge. We have to get the maximun number of each types of cubes, multiply them and add everyone's games.  
For expample:  
- Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green                          ----> 4 red * 2 green * 6 blue = 48
- Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue                ----> 1 red * 3 green * 4 blue = 12
- Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red        ----> 20 red * 13 green * 16 blue = 1560   
- Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red        ----> 14 red * 3 green * 15 blue = 630
- Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green                          ----> 6 red * 3 green * 2 blue = 36
- TOTAL   ---->  48 + 12 + 1560 + 630 + 36 = 2286

## DAY 3
### First challenge
After many hours trying this challenge I have copied it from https://github.com/Futarimiti/advent-of-code2023/blob/main/3-gear-rations/main.py .  
The 'prueba.py' file is my try, it doesn't work.  
The objective is add all numbers that are adjacent with an special symbols (NOT '.'). For example:  
- 467..114..
- ...*......
- ..35..633.
- ......#...
- 617*......
- .....+.58.
- ..592.....
- ......755.
- ...$.*....
- .664.598..
In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

### Second challenge
- I'm not going to say that is impossible but almost. (bro it is really hard)

## DAY 4
### First challenge
There are 2 rows separate by a '|'. The first represents winning numbers and the second the numbers you have. The objective is to know about hoy many numbers you have and then,
the first match makes the card worth one point and each match after the first doubles the point value of that card. For example:  
- Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53         --> {48, 83, 17, 86} ---> 8 points
- Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19         --> {32, 61}         ---> 2 points
- Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1         --> {1, 21}          ---> 2 points
- Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83         --> {84}             ---> 1 point
- Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36         --> {}               ---> 0 points
- Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11         --> {}               ---> 0 points
- Total  ----> 13 points
### Second challenge
- I will do it when I have enough time