class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        string = ''
        node = self.first

        while node is not None:
            if node.next is not None:
                string += str(node.value) + '-->'
            else:
                string += str(node.value)
            node = node.next
        return string

    def peek(self):
        return self.first

    def enqueue(self, value):
        node = Node(value)
        if self.length == 0:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        dequeueElement = self.first
        self.first = self.first.next
        self.length -= 1
        if self.length == 0:
            self.last = None
        return dequeueElement


myQueue = Queue()
myQueue.enqueue("Biden")
myQueue.enqueue("Trump")
myQueue.enqueue("Clinton")
# print(myQueue.peek().value)
print(str(myQueue))
# print(myQueue.dequeue().value)
myQueue.dequeue()
myQueue.dequeue()
myQueue.dequeue()
print(str(myQueue))
