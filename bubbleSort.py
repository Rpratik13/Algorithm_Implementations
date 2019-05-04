def bubbleSort(array: list) -> list:
	for i in range(len(array)):
		for j in range(i + 1, len(array)):
			if array[i] > array[j]:
				array[i], array[j] = array[j], array[i]
	return array


if __name__ == '__main__':
	print(bubbleSort([3, 4, 6, 2, 6, 2, 3, 68, 4, 1, 8, 3]))