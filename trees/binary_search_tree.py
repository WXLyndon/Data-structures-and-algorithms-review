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
        if self.root == None:
            return False
        current = self.root
        while current != None:
            if value < current.value:  # node shoude be in the left child of current
                if current.left:
                    current = current.left
                    continue
                return False  # not found
            elif value > current.value:  # node shoude be in the right child of current
                if current.right:
                    current = current.right
                    continue
                return False  # not found
            else:  # found
                return value

    def remove(self, value):
        if self.root == None: #Tree is empty
            return "Tree Is Empty"
        current_node = self.root
        parent_node = None
        while current_node!=None: #Traversing the tree to reach the desired node or the end of the tree
            if current_node.value > value:
                parent_node = current_node
                current_node = current_node.left
            elif current_node.value < value:
                parent_node = current_node
                current_node = current_node.right
            else: #Match is found. Different cases to be checked
                #Node has left child only
                if current_node.right == None:
                    if parent_node == None:
                        self.root = current_node.left
                        return
                    else:
                        if parent_node.value > current_node.value:
                            parent_node.left = current_node.left
                            return
                        else:
                            parent_node.right = current_node.left
                            return

                #Node has right child only
                elif current_node.left == None:
                    if parent_node == None:
                        self.root = current_node.right
                        return
                    else:
                        if parent_node.value > current_node.value:
                            parent_node.left = current_node.right
                            return
                        else:
                            parent_node.right = current_node.right
                            return

                #Node has neither left nor right child
                elif current_node.left == None and current_node.right == None:
                    if parent_node == None: #Node to be deleted is root
                        current_node = None
                        return
                    if parent_node.value > current_node.value:
                        parent_node.left = None
                        return
                    else:
                        parent_node.right = None
                        return

                #Node has both left and right child
                elif current_node.left != None and current_node.right != None:
                    del_node = current_node.right
                    del_node_parent = current_node.right
                    while del_node.left != None: #Loop to reach the leftmost node of the right subtree of the current node
                        del_node_parent = del_node
                        del_node = del_node.left
                    current_node.value = del_node.value #The value to be replaced is copied
                    if del_node == del_node_parent: #If the node to be deleted is the exact right child of the current node
                        current_node.right = del_node.right
                        return
                    if del_node.right == None: #If the leftmost node of the right subtree of the current node has no right subtree
                        del_node_parent.left = None
                        return
                    else: #If it has a right subtree, we simply link it to the parent of the del_node
                        del_node_parent.left = del_node.right
                        return
        return "Not Found"

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
# print(bst.lookup(8))
print(bst.lookup(5))
bst.remove(4)
bst.remove(8)
bst.remove(0)
bst.printTree()