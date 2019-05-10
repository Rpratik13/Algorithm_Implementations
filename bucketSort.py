from radixSort import radixSort

no_of_slots = 10

def bucketSort(array: list) -> list:
	div = max(array) // no_of_slots + 1
	result = list()
	sorted_array = list()
	for _ in range(no_of_slots):
		result.append([])
	
	for elem in array:
		result[elem // div].append(elem)

	print(result)
	for idx in range(len(result)):
		if len(result[idx]) != 0:
			result[idx] = radixSort(result[idx])
		

	for bucket in result:
		for elem in bucket:
			sorted_array.append(elem)

	return sorted_array


if __name__ == "__main__":
	print(bucketSort([41, 35, 93, 25, 22, 12, 3, 45, 45, 23, 63]))