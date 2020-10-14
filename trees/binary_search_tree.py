import json
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self,value):
        return NotImplemented

    def lookup(self, value):
        return NotImplemented

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
bst.root = BSTNode(1)
bst.printTree()