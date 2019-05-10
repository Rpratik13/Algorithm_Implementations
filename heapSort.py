def heapify(array: list, n: int, i: int):
	largest = i
	l = 2 * i + 1
	r = 2 * i + 2

	if (l < n) and (array[largest] < array[l]):
		largest = l

	if (r < n) and (array[largest] < array[r]):
		largest = r

	if largest != i:
		array[i], array[largest] = array[largest], array[i]
		heapify(array, n, largest)


def heapSort(array: list) -> None:
	n = len(array)

	for i in range((n - 1) // 2, -1, -1):
		heapify(array, n, i)

	for i in range(n - 1, -1, -1):
		array[0], array[i] = array[i], array[0]
		heapify(array, i, 0)


if __name__ == '__main__':
	array = [5, 4, 3, 2, 1, 3, 32, 6, 23]
	heapSort(array)
	print(array)