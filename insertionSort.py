def insertionSort(array: list) -> list:
	for i in range(1, len(array)):
		key = array[i]
		j = i - 1

		while j >= 0 and key < array[j]:
			array[j + 1] = array[j]
			j -= 1
		array[j + 1] = key
	return array

if __name__ == '__main__':
	print(insertionSort([2, 3, 5, 4, 3, 2, 1]))