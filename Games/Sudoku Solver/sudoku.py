puzzle = [
    [4,0,0,0,0,0,8,0,5],
    [0,3,0,0,0,0,0,0,0],
    [0,0,0,7,0,0,0,0,0],
    [0,2,0,0,0,0,0,6,0],
    [0,0,0,0,8,0,4,0,0],
    [0,0,0,0,1,0,0,0,0],
    [0,0,0,6,0,3,0,7,0],
    [5,0,0,2,0,0,0,0,0],
    [1,0,4,0,0,0,0,0,0],
]

def printPuzzle(puzzle):
    line = " -------------------------" 

    for i in range(len(puzzle)):
        if i % 3 == 0:
            print(line)
        for v in range(len(puzzle[i])):
            if v % 3 == 0:
                print(" |", end='')
            print(" ", puzzle[i][v], sep='', end='')
        print(" |")
    print (line)

printPuzzle(puzzle)

