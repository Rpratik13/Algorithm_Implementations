def merge(left: list, right: list) -> list:
	leftIndex = rightIndex = 0
	merged = list()
	while leftIndex < len(left) and rightIndex < len(right):
		if left[leftIndex] < right[rightIndex]:
			merged.append(left[leftIndex])
			leftIndex += 1
		else:
			merged.append(right[rightIndex])
			rightIndex += 1

	for i in range(leftIndex, len(left)):
		merged.append(left[i])

	for i in range(rightIndex, len(right)):
		merged.append(right[i])

	return merged


def mergeSort(array: list) -> list:
	if len(array) > 1:
		left = mergeSort(array[:len(array) // 2])
		right = mergeSort(array[len(array) // 2:])
		array = merge(left, right)
	return array

if __name__ == '__main__':
	print(mergeSort([2, 1, 5, 3, 6, 2]))