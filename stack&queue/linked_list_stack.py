class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
    
    def __str__(self):
        string = ''
        node = self.top

        while node is not None:
            if node.next is not None:
                string += str(node.value) + '-->'
            else:
                string += str(node.value)
            node = node.next
        return string

    def peek(self):
        return self.top
    
    def push(self, value):
        node = Node(value)
        if self.length == 0:
            self.top = node
            self.bottom = node
        else:
            olderTop = self.top
            self.top = node
            self.top.next = olderTop
        self.length += 1
    
    def pop(self):
        if self.length == 0:
            return None
        popElement = self.top
        self.top = self.top.next
        self.length -= 1
        if self.length == 0:
            self.bottom = None
        return popElement
        

myStack = Stack()
myStack.push("Google")
myStack.push("Twitter")
myStack.push("Facebook")
# print(myStack.peek().value) 
print(str(myStack))
myStack.pop()
myStack.pop()
myStack.pop()
print(str(myStack))