import numpy as np # Display cool matrix in terminal

# Sudoku
# TODO read the image and fill the matrix
sudoku = [[1,0,0,0,0,0,0,0,0],[0,0,0,4,0,0,0,0,0],[0,0,0,0,0,0,9,0,0],
        [0,0,5,0,0,0,0,0,0],[0,2,0,0,0,0,0,0,0],[0,0,0,0,0,0,7,0,0],
        [0,0,0,0,0,0,0,0,3],[0,6,0,0,0,0,0,0,0],[0,0,0,0,0,8,0,0,0]]
print(np.matrix(sudoku))

# x (row) and y(column) are position, n is a number
# check if it's possible to put n in [y,x] the row, column and square is that order
def possible(y,x,n) :
    global sudoku
    for i in range(0,9):
        if sudoku[y][i] == n :
            return False
    for i in range(0,9):
        if sudoku[i][x] == n :
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if sudoku[y0+i][x0+j] == n :
                return False
    return True

def solve():
    global sudoku
    for y in range(9):
        for x in range(9):
            #check if there is an empty field
            if sudoku[y][x] == 0:
                #check every number for this field
                for n in range(1,10):
                    if possible(y,x,n):
                        sudoku[y][x] = n
                        # Try to solve the next empty field
                        solve()
                        # Backtracking.. if we are here it means there is no possible solution
                        # The field needs to be reset and the previous function solve() will continue with n+1
                        sudoku[y][x] = 0
                return #no solution
    # Every field has a number
    print(np.matrix(sudoku))
    # Give the prompt to the user to only display one solution at the time
    input("Need more solutions ?") 
    
solve()
# No more solution