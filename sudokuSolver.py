def printBoard(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=' ')
        print('')

        
def findEmpty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j

def isSafe(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    for i in range(3):
        for j in range(3):
            if board[row - row % 3 + i][col - col % 3 + j] == num:
                return False

    return True


def isCompleted(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return False
    return True


def sudokuSolver(board):
    if isCompleted(board):
        return True

    row, col = findEmpty(board)

    for i in range(1, 10):
        if isSafe(board, row, col, i):
            board[row][col] = i

            if sudokuSolver(board):
                return True

            board[row][col] = 0
    return False


if __name__ == '__main__':
    board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    # board = [[3,0,6,5,0,8,4,0,0], 
    #          [5,2,0,0,0,0,0,0,0], 
    #          [0,8,7,0,0,0,0,3,1], 
    #          [0,0,3,0,1,0,0,8,0], 
    #          [9,0,0,8,6,3,0,0,5], 
    #          [0,5,0,0,9,0,6,0,0], 
    #          [1,3,0,0,0,0,2,5,0], 
    #          [0,0,0,0,0,0,0,7,4], 
    #          [0,0,5,2,0,6,3,0,0]] 

    if sudokuSolver(board):
        printBoard(board)
    else:
        print('No solution')