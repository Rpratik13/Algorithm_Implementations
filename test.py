from countingSort import countingSort
from radixSort import radixSort
from bucketSort import bucketSort
import matplotlib.pyplot as plt
import time


if __name__ == "__main__":
	n = 100000
	num = list()
	times = list()
	x = time.time()
	print(x)
	for i in range(n, n * 10 + 1, n):
		array = list(range(i))[::-1]
		# start_time = time.time()
		# temp = countingSort(array)
		# end_time = time.time()


		# print("For counting sort: {}".format(end_time - start_time))
		# start_time = time.time()
		# temp = radixSort(array)
		# end_time = time.time()
		# print("For radix sort: {}".format(end_time - start_time))

		# start_time = time.time()
		# temp = bucketSort(array)
		# end_time = time.time()
		# print("For bucket sort: {}\n".format(end_time - start_time))
		# times.append(end_time - start_time)
		# num.append(i)

	# plt.plot(times)
	# plt.show()	