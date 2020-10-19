# Leetcode Q232
class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) == 0:
            return None
        popElement = self.stack[0]
        self.stack = self.stack[1:]
        return popElement

    def peek(self):
        if len(self.stack) == 0:
            return None
        return self.stack[0]

    def isEmpty(self):
        return len(self.stack) == 0


myQueue = MyQueue()
myQueue.push("Biden")
myQueue.push("Trump")
myQueue.push("Clinton")
print(myQueue.stack)
print(myQueue.pop())
print(myQueue.pop())
print(myQueue.pop())
# print(myQueue.pop())
print(myQueue.stack)
