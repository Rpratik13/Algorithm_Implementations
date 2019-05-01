def countingSort(array: list) -> list:
	count = [0] * (max(array) + 1)
	sort = [None] * len(array)

	for i in array:
		count[i] += 1

	for i in range(1, len(array)):
		count[i] += count[i - 1]
	
	for i in array[::-1]:
		sort[count[i] - 1] = i
		count[i] -= 1
	return sort


if __name__ == '__main__':
	print(countingSort([3, 4, 1, 6, 3, 7, 5, 8]))