from radixSort import radixSort

def bucketSort(array: list) -> list:
	m = 10 ** (len(str(max(array))) - 1)
	result = list()
	sorted_array = list()
	for _ in range(m):
		result.append([])
	
	for elem in array:
		result[elem // m].append(elem)

	for idx in range(len(result)):
		if len(result[idx]) != 0:
			result[idx] = radixSort(result[idx])
		

	for bucket in result:
		for elem in bucket:
			sorted_array.append(elem)

	return sorted_array


if __name__ == "__main__":
	print(bucketSort([41, 353, 22, 12345, 45, 23, 63]))