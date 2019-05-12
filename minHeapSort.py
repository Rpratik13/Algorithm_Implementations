def heapify(array: list, n: int, i: int) -> None:
	smallest = i
	l = 2 * i + 1
	r = 2 * i + 2

	if (l < n) and (array[smallest] > array[l]):
		smallest = l

	if (r < n) and (array[smallest] > array[r]):
		smallest = r

	if (smallest != i):
		array[i], array[smallest] = array[smallest], array[i]
		heapify(array, n, smallest)


def minHeapSort(array: list) -> None:
	n = len(array)

	for i in range(n, -1, -1):
		heapify(array, n, i)

	for i in range(n - 1, -1, -1):
		array[0], array[i] = array[i], array[0]
		heapify(array, i, 0)

if __name__ == '__main__':
	array = [5, 6, 30, 20, 23, 21, 1]
	minHeapSort(array)
	print(array)