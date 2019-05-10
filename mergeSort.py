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

	if leftIndex < len(left):
		merged.extend(left[leftIndex:])
	else:
		merged.extend(right[rightIndex:])

	return merged


def mergeSort(array: list) -> list:
	if len(array) > 1:
		left = mergeSort(array[:len(array) // 2])
		right = mergeSort(array[len(array) // 2:])
		array = merge(left, right)
	return array

if __name__ == '__main__':
	print(mergeSort([2, 1, 5, 3, 6, 2]))