class Stack:
    def __init__(self):
        self.array = []

    def peek(self):
        return self.array[-1]
    
    def push(self, value):
        self.array.append(value)
    
    def pop(self):
        return self.array.pop()
        

myStack = Stack()
myStack.push("Google")
myStack.push("Twitter")
myStack.push("Facebook")
print(myStack.array)
myStack.pop()
myStack.pop()
print(myStack.array)
myStack.pop()
print(myStack.array)