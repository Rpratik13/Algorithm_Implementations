def selectionSort(array: list) -> list:
	for i in range(len(array) - 1):
		minIndex = i
		for j in range(i + 1, len(array)):
			if array[j] < array[minIndex]:
				minIndex = j
		array[i], array[minIndex] = array[minIndex], array[i]


def recursiveSelectionSort(array: list) -> list:
	if len(array) > 1:
		minIndex = 0
		for index in range(1, len(array)):
			if array[index] < array[minIndex]:
				minIndex = index
		array[0], array[minIndex] = array[minIndex], array[0]
		array = array[:1] + recursiveSelectionSort(array[1:])
	return array


if __name__ == '__main__':
	# array = random.sample(range(1, 1000), 500)
	array = [5, 3, 2, 10 , 1 , 9]
	selectionSort(array)
	print(array)
	print(recursiveSelectionSort(array))
	