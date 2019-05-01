def binarySearch(array: list, target: int) -> int:
	left = 0
	right = len(array)
	mid = (left + right) // 2


	while (left <= right) and (mid in range(len(array))):

		if array[mid] == target:
			return mid
		elif array[mid] > target:
			right = mid - 1
		else:
			left = mid + 1
		mid = (left + right) // 2
	return -1


def recursiveBinarySearch(array: list, target: int, left: int, right: int) -> int:
	mid = (left + right) // 2
	if (left <= right) and (mid in range(len(array))):
		

		if array[mid] == target:
			return mid
		elif array[mid] > target:
			return recursiveBinarySearch(array, target, left, mid - 1)
		else:
			return recursiveBinarySearch(array, target, mid + 1, right)
	return -1


if __name__ == '__main__':
	array = [int(i) for i in input().split()]
	target = int(input())
	print(binarySearch(array, target))