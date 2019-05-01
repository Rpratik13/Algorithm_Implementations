def radixSort(array: list) -> list:
	for pw in range(1, len(str(max(array))) + 1):
		digits = list()
		for elem in array:
			digit = elem % (10 ** pw) // (10 ** (pw - 1))
			digits.append(digit)

		count = [0] * (max(digits) + 1)
		sort = [None] * len(array)
		for elem in array:
			digit = elem % (10 ** pw) // (10 ** (pw - 1))
			count[digit] += 1

		for i in range(1, len(count)):
			count[i] += count[i - 1]

		for elem in array[::-1]:
			digit = elem % (10 ** pw) // (10 ** (pw - 1))
			sort[count[digit] - 1] = elem
			count[digit] -= 1
		array = sort
	return array


if __name__ == '__main__':
	print(radixSort([142, 22, 41, 45, 23, 16, 51, 27]))

