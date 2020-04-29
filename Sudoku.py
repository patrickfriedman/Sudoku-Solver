from random import randrange

def diff(difficulty):                                      #players difficulty
    if (difficulty == 0):
        shown = 55
    elif (difficulty == 1):
        shown = 45
    elif (difficulty == 2):
        shown = 35
    return shown

def newBoard():                                             #creates an empty board
    board = [[0 for x in range(9)] for y in range(9)]
    return board

def newGame(nb, sb, diff):                                  #creates solvable board per difficulty for user
    for x in range(diff):
        x = randrange(9)
        y = randrange(9)
        nb[x][y] = sb[x][y]

    return nb

def printBoard(b):                                           #print boards in nice format
    print()
    for i in range(len(b)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(b[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end = "")
            if j == 8:
                print(b[i][j])
            else:
                print(str(b[i][j]) + " ", end = "")
                
def find_unsolved(b):                                        #look for unsolved position
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                return (i, j)

    return None

def correct(b, num, pos):                                    #check each constraint
    #row
    for i in range(len(b[0])):
        if b[pos[0]][i] == num and pos[1] != i:
            return False

    #column
    for i in range(len(b)):
        if b[i][pos[1]] == num and pos[0] != i:
            return False

    #grid
    grid_x = pos[1] // 3
    grid_y = pos[0] // 3

    for i in range(grid_y * 3, grid_y * 3 + 3):
        for j in range(grid_x * 3, grid_x * 3 + 3):
            if b[i][j] == num and (i, j) != pos:
               return False

    return True 

def solve(b):                                                 #solve recursively
    find = find_unsolved(b)
    if not find:
        return True
    else:
        row, col = find

    for x in range(1, 10):
        x = randrange(10)                                     #creates random starting number for uniqueness
        if correct(b, x, (row, col)):
            b[row][col] = x

            if solve(b):
                return True

            b[row][col] = 0
    return False

def textGame():
    sb = newBoard()                                           #create an empty board
    solve(sb)                                                 #solves new board

    printBoard(newGame(newBoard(), sb, diff(0)))              #creates a game board that can be solved per difficulty
    print()
    input("Press Enter for the Solution: ")
    printBoard(sb)                                            #prints solved board

#textGame()                                                   #use to run game in text editor