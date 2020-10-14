import json


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = BSTNode(value)
        if self.root == None:
            self.root = node
            return
        current = self.root
        while current != None:
            if value <= current.value:  # node shoude be inserted in the left child of current
                if current.left:
                    current = current.left
                    continue
                current.left = node
                return
            else:  # node shoude be inserted in the right child of current
                if current.right:
                    current = current.right
                    continue
                current.right = node
                return

    def lookup(self, value):
        current = self.root
        while current != None:
            if value < current.value:  # node shoude be in the left child of current
                if current.left:
                    current = current.left
                    continue
                return None  # not found
            elif value > current.value:  # node shoude be in the right child of current
                if current.right:
                    current = current.right
                    continue
                return None  # not found
            else:  # found
                return value

    def remove(self, value):
        return NotImplemented

    def printTree(self):
        if self.root != None:
            self.inorderPrintTree(self.root)

    def inorderPrintTree(self, node):
        if node != None:
            self.inorderPrintTree(node.left)
            print(node.value)
            self.inorderPrintTree(node.right)


bst = BST()
bst.insert(1)
bst.insert(2)
bst.insert(0)
bst.insert(8)
bst.insert(4)
bst.printTree()
print(bst.lookup(8))
print(bst.lookup(5))

