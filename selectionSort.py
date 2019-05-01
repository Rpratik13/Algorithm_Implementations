def selectionSort(array: list) -> list:
	for i in range(len(array) - 1):
		minIndex = i
		for j in range(i + 1, len(array)):
			if array[j] < array[minIndex]:
				minIndex = j
		array[i], array[minIndex] = array[minIndex], array[i]
	return array


def recursiveSelectionSort(array: list) -> list:
	if len(array) > 1:
		minIndex = 0
		for index in range(1, len(array)):
			if array[index] < array[minIndex]:
				minIndex = index
		array[0], array[minIndex] = array[minIndex], array[0]
		array = array[:1] + selectionSort(array[1:])
	return array


if __name__ == '__main__':
	array = random.sample(range(1, 1000), 500)
	print(selectionSort(array))
	print(recursiveSelectionSort(array))
	