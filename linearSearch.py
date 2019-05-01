def linearSearch(array: list, target: int) -> int:
	for idx in range(len(array)):
		if array[idx] == target:
			return idx
	return -1


if __name__ == '__main__':
	array = [int(i) for i in input().split()]
	target = int(input())
	print(linearSearch(array, target))