class BinarySearchTree:

	def __init__(self):
		self.root = None


	def insert(self, value=None)-> None:
		if self.root == None:
			self.root = Node(value)
		else:
			self._insert(value, self.root)


	def _insert(self, value: int, current_node) -> None:
		if value < current_node.value:
			if current_node.left == None:
				current_node.left = Node(value)
			else:
				return self._insert(value, current_node.left)
		elif value > current_node.value:
			if current_node.right == None:
				current_node.right = Node(value)
			else:
				return self._insert(value, current_node.right)
		else:
			print('{} is already in tree.'.format(value))


	def traverse(self, mode) -> None:
		if self.root != None:
			if mode == "pre":
				return self._preorderTraverse(self.root)
			elif mode == 'in':
				return self._inorderTraverse(self.root)
			elif mode == 'post':
				return self._postorderTraverse(self.root)


	def _preorderTraverse(self, current_node) -> None:
		if current_node != None:
			print(current_node.value)
			self._traverse(current_node.left)
			self._traverse(current_node.right)


	def _inorderTraverse(self, current_node) -> None:
		if current_node != None:
			self._traverse(current_node.left)
			print(current_node.value)
			self._traverse(current_node.right)
			

	def _postorderTraverse(self, current_node) -> None:
		if current_node != None:
			self._traverse(current_node.left)
			self._traverse(current_node.right)
			print(current_node.value)
			

	def height(self):
		if self.root == None:
			return 0
		return self._height(self.root, current_height=0)


	def _height(self, current_node, current_height):
		if current_node == None:
			return current_height
		left_height = self._height(current_node.left, current_height + 1)
		right_height = self._height(current_node.right, current_height + 1)
		return max(left_height, right_height)


	def search(self, target):
		if self.root != None:
			return self._search(target, self.root)
		return False


	def _search(self, target, current_node):
		if current_node.value == target:
			return True
		elif target < current_node.value and current_node.left != None:
			return self._search(target, current_node.left)
		elif target > current_node.value and current_node.right != None:
			return self._search(target, current_node.right)
		else:
			return False


class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


if __name__ == '__main__':
	array = [2, 3, 6, 4, 1, 2, 7, 7, 3]
	bt = BinarySearchTree()
	bt.insert(2)
	bt.insert(3)
	bt.insert(3)
	print(bt.search(3))
	print(bt.search(4))
	# bt.traverse()