def partition(array: list) -> list:
	i = 1
	j = len(array) - 1
	while i < j:
		while array[i] < array[0]:
			i += 1

		while array[j] > array[0]:
			j -= 1

		if i < j:
			array[i], array[j] = array[j], array[i]

	array[j], array[0] = array[0], array[j]

	return quickSort(array[:j]) + [array[j]] + quickSort(array[j + 1:])


def quickSort(array: list) -> list:
	if len(array) > 1:
		return partition(array)
	return array


if __name__ == '__main__':
	print(quickSort([2, 5, 1, 3, 2, 4, 6]))