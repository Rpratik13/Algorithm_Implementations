no_of_slots = 10

class LinkedList:

	def __init__(self):
		self.root = None
		self.next = None

	def insert(self, value):
		if self.root == None:
			self.root = Node(value)
		else:
			return self._insert(self.root, value)


	def _insert(self, currentNode, value):
		if currentNode.next == None:
			currentNode.next = Node(value)
		else:
			return self._insert(currentNode.next, value)


	def display(self):
		if self.root != None:
			return self._display(self.root)

	def _display(self, currentNode):
		print(currentNode.value)
		if currentNode.next != None:
			return self._display(currentNode.next)


	def search(self, key):
		position = 0
		if self.root != None:
			return self._search(self.root, key, position)


	def _search(self, currentNode, key, position):
		if currentNode.value  == key:
			return position
		elif currentNode.next != None:
			return self._search(currentNode.next, key, position + 1)
		else:
			return -1
class Node:

	def __init__(self, value):
		self.value = value
		self.next = None



def hashing(key):
	return key % no_of_slots


if __name__ == '__main__':
	array = list(range(1, 51))
	hashed = []
	for i in range(no_of_slots):
		hashed.append(LinkedList())

	for i in array:
		hashed[i % no_of_slots].insert(i)

	hashed[3].display()

	key = 33
	print(hashed[key % no_of_slots].search(key))