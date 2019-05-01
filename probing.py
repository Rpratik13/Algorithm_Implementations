c1 = 0
c2 = 1
m = 7

def hashing(key):
	return key % m


def probing(array: list) -> list:
	result = [None] * m
	for elem in array:
		hsh = hashing(elem)
		i = 1
		while result[hsh] != None:
			hsh = (hashing(elem) + c1 * i + c2 * (i ** 2)) % m
			i += 1
		result[hsh] = elem
	return result


if __name__ == '__main__':
	array = [1, 8, 15]
	hashed = probing(array)
	for i, j in enumerate(hashed):
		print("{}: {}".format(i, j))