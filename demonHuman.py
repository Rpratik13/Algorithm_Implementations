def isSafe(island1, island2):
	if len(island1) + len(island2) != 6:
		return False

	if island1.count('H') != 0 and island1.count('H') < island1.count('D'):
		return False

	if island2.count('H') != 0 and island2.count('H') < island2.count('D'):
		return False	

	return True

boat_on_left = [False]
moved = [False]
last_move = ['x']

def move(toIsland, fromIsland, move):
	if move == 'dd':
		if fromIsland.count('D') >= 2:
			for i in range(2):
				fromIsland.remove('D')
				toIsland.append('D')
				moved[0] = True
	elif move == 'dh':
		if fromIsland.count('D') >= 1 and fromIsland.count('H') >= 1:
			fromIsland.remove('D')
			fromIsland.remove('H')
			toIsland.append('D')
			toIsland.append('H')
			moved[0] = True
	elif move == 'hh':
		if fromIsland.count('H') >= 2:
			for i in range(2):
				fromIsland.remove('H')
				toIsland.append('H')
				moved[0] = True
	elif move == 'd':
		if fromIsland.count('D') >= 1:
			fromIsland.remove('D')
			toIsland.append('D')
			moved[0] = True
	elif move == 'h':
		if fromIsland.count('H') >= 1:
			fromIsland.remove('H')
			toIsland.append('H')
			moved[0] = True
	
	if moved[0]:
		last_move[0] = move
		boat_on_left[0] = not boat_on_left[0]
		


def solveDH(left, right):
	moved[0] = False
	if len(left) != 6:
		for i in ['dd', 'dh', 'hh', 'd', 'h']:
			
			if i != last_move[0]:
				if boat_on_left[0]:
					move(right, left, i)
				else:
					move(left, right, i)
				if not moved[0]:
					continue

				if not isSafe(left, right):
					if boat_on_left[0]:
						move(left, right, i)
					else:
						move(right, left, i)
					return False

				else:
					print("left: {}".format(left))
					print("right: {}".format(right))
					print('')
					if solveDH(left, right):
						return True
					else:
						if boat_on_left[0]:
							move(left, right, i)
						else:
							move(right, left, i)

	else:
		return True


toIsland = []
fromIsland = ['D', 'D', 'D', 'H', 'H', 'H']
solveDH(toIsland, fromIsland)
# fromIsland = ['D', 'D']
# toIsland = ['D', 'H', 'H', 'H']
# move(toIsland, fromIsland, 'd')
# print()
print(toIsland)
print(fromIsland)
print(boat_on_left)
