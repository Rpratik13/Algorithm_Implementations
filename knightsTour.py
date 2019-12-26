for i in range(n):
	for j in range(n):
		next_moves.append([])

def isSafe(board, current_row, current_col, row, col):
	if abs(current_row - row) + abs(current_col - col) == 3 and board[row][col] == 0:
		return True
	return False


def isCompleted(board):
	for i in range(n):
		for j in range(n):
			if board[i][j] == 0:
				return False
	return True


def knightsTour(board, step, row, col):
	if isCompleted(board):
		return True

	for i in next_moves
