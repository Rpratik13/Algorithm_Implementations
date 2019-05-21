class NilNode():
    def __init__(self):
        self.value = 'nil'
        self.color = 'b'
        self.parent = None

class Node():
    def __init__(self, value=None, color='r'):
        self.value = value
        self.color = color
        self.left = NilNode()
        self.right = NilNode()
        self.parent = None

    def recolor(self):
        if self.color == 'b':
            self.color = 'r'
        else:
            self.color = 'b'


nil_node = Node(color='b')

class RedBlackTree():
    def __init__(self):
        self.root = None


    def leftRotate(self, currentNode):
        x = currentNode
        y = x.right
        if y.left != nil_node:
            x.right = y.left
            x.right.parent = x
        if x.parent == None:
            self.root = y
        else:
            if x.parent.left == x:
                x.parent.left = y
            else:
                x.parent.right = y
            y.parent = x.parent
        y.left = x
        x.parent = y
        currentNode = y
        
    def rightRotate(self, currentNode):
        x = currentNode
        y = x.left
        if y.right != nil_node:
            x.left = y.right
            x.left.parent = x
        if x.parent == None:
            y.parent = None
            self.root = y
        else:
            if x.parent.left == x:
                x.parent.left = y
            else:
                x.parent.right = y
            y.parent = x.parent
        y.right = x
        x.parent = y
        currentNode = y


    def insert(self, value):
        if self.root == None:
            self.root = Node(value=value)
            self.root.color = 'b'
        else:
            return self._insert(self.root, value)

    def _insert(self, currentNode, value):
        if currentNode.value > value:
            if currentNode.left.value == 'nil':
                currentNode.left = Node(value=value)
                currentNode.left.parent = currentNode
                self.insertCheck(currentNode.left)
            else:
                return self._insert(currentNode.left, value)
        else:
            if currentNode.right.value == 'nil':
                currentNode.right = Node(value=value)
                currentNode.right.parent = currentNode
                self.insertCheck(currentNode.right)
            else:
                return self._insert(currentNode.right, value)

    def insertCheck(self, currentNode):
        if currentNode != self.root and currentNode.parent != self.root and currentNode.parent.color != 'b':
            if currentNode.parent.parent.left == currentNode.parent:
                if currentNode.parent.parent.right.color == 'r':
                    currentNode.parent.recolor()
                    currentNode.parent.parent.recolor()
                    currentNode.parent.parent.right.recolor()
                    self.insertCheck(currentNode.parent.parent)
                else:
                    if currentNode.parent.left == currentNode:
                        currentNode.parent.parent.color, currentNode.parent.color = currentNode.parent.color, currentNode.parent.parent.color
                        self.rightRotate(currentNode.parent.parent)
                    else:
                        self.leftRotate(currentNode.parent)
                        # print(currentNode.left.value)
                        self.insertCheck(currentNode.left)
            else:
                if currentNode.parent.parent.left.color == 'r':
                    currentNode.parent.recolor()
                    currentNode.parent.parent.recolor()
                    currentNode.parent.parent.left.recolor()
                else:
                    if currentNode.parent.right == currentNode:
                        currentNode.parent.parent.color, currentNode.parent.color = currentNode.parent.color, currentNode.parent.parent.color
                        self.leftRotate(currentNode.parent.parent)
                    else:
                        self.rightRotate(currentNode.parent)
                        self.insertCheck(currentNode.right)

            self.root.color = 'b'

    def largestKey(self):
        if self.root != None:
            return self._largestKey(self.root)
        return None


    def _largestKey(self, current_node):
        if current_node.right.value != 'nil':
            return self._largestKey(current_node.right)
        return current_node.value, current_node.color

    def delete(self, key):
        if self.root != None:
            return self._delete(self.root, key)


    def _delete(self, current_node, key):
        color = 'r'
        if current_node.value == key:
            if current_node.value != 'nil' and current_node.right.value != 'nil':
                max_val, max_color = self._largestKey(current_node.left)
                self.delete(max_val)
                current_node.value = max_val
                if current_node.color == 'r' or max_color == 'r':
                    current_node.color = 'b'
            elif current_node.left.value != 'nil':
                if current_node == self.root:
                    deleted_node = self.root
                    replaced_node = self.root.left
                    if deleted_node.color == 'r' or replaced_node.color == 'r':
                        self.root.left.color = 'b'
                    self.root = self.root.left

                elif current_node.parent.left.value == key:
                    deleted_node = current_node.parent.left
                    replaced_node = current_node.left
                    if deleted_node.color == 'r' or replaced_node.color == 'r':
                        current_node.left.color = 'b'
                    current_node.parent.left = current_node.left
                else:
                    deleted_node = current_node.parent.right
                    replaced_node = current_node.left
                    if deleted_node.color == 'r' or replaced_node.color == 'r':
                        current_node.left.color = 'b'
                    current_node.parent.right = current_node.left

                deleted_node.color = color
            elif current_node.right.value != 'nil':
                if current_node == self.root:
                    deleted_node = self.root
                    replaced_Node = self.root.right
                    if deleted_node.color == 'r' or replaced_node.color == 'r':
                        color = 'b'
                    self.root = self.root.right
                elif current_node.parent.left.value == key:
                    deleted_node = current_node.parent.left
                    replaced_node = current_node.right
                    if deleted_node.color == 'r' or replaced_node.color == 'r':
                        current_node.right.color = 'b'
                    current_node.parent.left = current_node.right
                else:
                    deleted_node = current_node.parent.right
                    replaced_node = current_node.right
                    if deleted_node.color == 'r' or replaced_node.color == 'r':
                        current_node.right.color = 'b'
                    current_node.parent.right = current_node.right
                deleted_node.color = color            
            else:
                if current_node == self.root:
                    self.root = None
                elif current_node.parent.left.value == key:
                    current_node.parent.left = NilNode()
                else:
                    current_node.parent.right = NilNode()
        elif current_node.value < key:
            if current_node.right.value != 'nil':
                return self._delete(current_node.right, key)
            else:
                print('{} not in tree.'.format(key))
        else:
            if current_node.left.value != 'nil':
                return self._delete(current_node.left, key)
            else:
                print('{} not in tree.'.format(key))
        

    def traverse(self, mode='pre'):
        if self.root != None:
            if mode == 'pre':
                return self._preOrder(self.root)
            elif mode == 'in':
                return self._inOrder(self.root)
            else:
                return self._postOrder(self.root)

    def _preOrder(self, currentNode):
        if currentNode.value != 'nil':
            print('{} {}'.format(currentNode.value, currentNode.color))
            self._preOrder(currentNode.left)
            self._preOrder(currentNode.right)

    def _inOrder(self, currentNode):
        if currentNode.value != 'nil':
            self._preOrder(currentNode.left)
            print(currentNode.value)
            self._preOrder(currentNode.right)

    def _postOrder(self, currentNode):
        if currentNode.value != 'nil':
            self._postOrder(currentNode.left)
            self._postOrder(currentNode.right)
            print(currentNode.value)

    def searchRotate(self, value):
        if self.root != None:
            return self._searchRotate(self.root, value)

    def _searchRotate(self, currentNode, value):
        if currentNode.value == value:
            return self.rightRotate(currentNode)
        elif currentNode.value > value:
            return self._searchRotate(currentNode.left, value)
        else:
            return self._searchRotate(currentNode.right, value)


if __name__ == '__main__':
    tree = RedBlackTree()
    # array = [5, 2, 1, 3, 7]
    array = [30, 15, 45, 10, 20, 55, 59, 65, 58]
    for i in array:
        tree.insert(i)
    # tree.delete()
    # tree.delete(10)
    tree.traverse('pre')