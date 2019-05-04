m = 7

def hash1(key: int) -> int:
	return key % m


def hash2(key: int) -> int:
	return 5 * key + 2


def doubleHashing(array: list) -> list:
	hashed = [None] * m
	for elem in array:
		hsh = hash1(elem)
		i = 1
		while hashed[hsh] != None:
			hsh = (hash1(elem) + i * hash2(elem)) % m
			i += 1

		hashed[hsh] = elem
	return hashed


if __name__ == '__main__':
	array = [27, 5, 8, 10, 13]
	for idx, val in enumerate(doubleHashing(array)):
		if val != None:
			print("{}: {} ".format(idx, val))

