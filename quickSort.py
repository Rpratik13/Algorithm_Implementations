def partition(array: list, pivot: int) -> list:
	lesser = list()
	greater = list()
	for elem in array:
		if elem < pivot:
			lesser.append(elem)
		else:
			greater.append(elem)
	
	return quickSort(lesser) + [pivot] + quickSort(greater)


def quickSort(array: list) -> list:
	if len(array) > 1:
		pivot = array[0]
		return partition(array[1:], pivot)
	return array


if __name__ == '__main__':
	print(quickSort([2, 5, 1, 3, 2, 4, 6]))