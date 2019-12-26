n = 4

def printSolution(solution):
	for i in range(n):
		for j in range(n):
			print(solution[i][j], end=' ')
		print('')


def isSafe(maze, x, y):
	if 0 <= x < n and 0 <= y < n and maze[x][y] == 1:
		return True
	return False


def solveMaze(maze, x, y, solution):
	if solution[n - 1][n - 1] == 1:
		return True

	if isSafe(maze, x, y):
		solution[x][y] = 1

		if solveMaze(maze, x, y + 1, solution):
			return True

		if solveMaze(maze, x + 1, y, solution):
			return True


		solution[x][y] = 0
		return False


if __name__ == "__main__": 
	maze = [[1, 1, 0, 1],
			[0, 1, 0, 1],
			[1, 1, 0, 1],
			[1, 1, 1, 1]]
	
	solution = list()
	for i in range(n):
		row = list()
		for j in range(n):
			row.append(0)
		solution.append(row)
	if solveMaze(maze, 0, 0, solution):
		printSolution(solution)
	else:
		print("No Solution")