gameBoard = [
    [0,9,3,8,6,0,2,1,4],
    [0,1,8,3,9,0,0,7,0],
    [0,4,6,0,5,0,0,0,0],
    [0,0,1,5,8,0,9,2,7],
    [0,0,0,7,3,9,0,0,0],
    [0,0,7,4,0,1,0,0,0],
    [0,6,4,9,7,5,3,0,0],
    [8,0,9,0,1,0,0,4,0],
    [3,0,5,0,4,0,1,0,9],
]

def printBoard(board):
    # prints current game board
    for row in range(len(board)):
        if (row) % 3 == 0 and row != 0:
            print("- - - - - - - - - - -")

        for num in range(len(board[row])):
            if (num+1)%3 == 0 and num != 8:
                print(str(board[row][num]) + " | ", end="")
            else:
                print(board[row][num], end=" ")

        print("")

def checkValid(board, num, pos):
    # given the parameters, check if
    # the number is valid by checking
    # current row, column, and box

    # checks current row
    for i in range(len(board[pos[0]])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # checks current column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
        
    # checks current box

    # divides it into 3x3 boxes
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    # iterates from beginning index - end index   
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False
    
    return True

def findEmpty(board):
    # goes through game board and
    # returns positions of zeros 
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == 0:
                return (row, column)

    return None

def solvePuzzle(board):
    # solve puzzle recursively with backtracking algorithm

    find = findEmpty(board)

    if find != None:
        row = find[0]
        column = find[1]
        
    else:
        return True
    
    for i in range(0,9):
        # if input number is valid, assign value
        # to current position on the grid
        if checkValid(board, i+1, (row, column)):
            board[row][column] = i+1

            # if inputs of 1-9 aren't valid,
            # assigns 0 to current position
            # and backtracks to prior index
            if solvePuzzle(board):
                return True
            else:
                board[row][column] = 0

    return False

printBoard(gameBoard)
solvePuzzle(gameBoard)
print('~~~~~~~~~~~~~~~~~~~~~')
printBoard(gameBoard)