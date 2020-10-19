import sys


class MaxHeap:

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        # Our MaxHeap index starts with 1.
        self.heap = [0] * (self.maxsize + 1)
        # So heap[0] is filled with the garbage value.
        self.heap[0] = sys.maxsize
        self.front = 1

    def print_heap(self):
        for i in range(1, (self.size // 2) + 1):
            heapString = "PARENT: "
            heapString += str(self.heap[i]) + ", "
            heapString += "LEFT CHILD: " + str(self.heap[2 * i]) + ", "
            heapString += "RIGHT CHILD: " + str(self.heap[2 * i + 1])
            print(heapString)

    def parent(self, index):
        return index // 2

    def left_child(self, index):
        return 2 * index

    def right_child(self, index):
        return (2 * index) + 1

    def is_leaf(self, index):
        return (index > self.size // 2) and index <= self.size

    def swap(self, first, second):
        self.heap[first], self.heap[second] = self.heap[second], self.heap[first]

    def max_heapify(self, index):

        # if the node is a non-leaf node
        if not self.is_leaf(index):
            left_index = self.left_child(index)
            right_index = self.right_child(index)

            # if the node is smaller than any of its child
            if (self.heap[index] < self.heap[left_index]) or (self.heap[index] < self.heap[right_index]):

                # Left child is bigger than right child.
                if self.heap[left_index] > self.heap[right_index]:
                    # swap the node and its left child.
                    self.swap(index, left_index)
                    # max heapify the left child.
                    self.max_heapify(left_index)

                # Right child is bigger than or equal to right child.
                else:
                    self.swap(index, right_index)
                    # max heapify the left child.
                    self.max_heapify(right_index)

    def insert(self, value):
        if self.size >= self.maxsize:
            return

        self.size += 1
        self.heap[self.size] = value
        current = self.size

        while self.heap[current] >= self.heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def extract_max(self):
        popElement = self.heap[self.front]
        self.heap[self.front] = self.heap[self.size]
        self.heap[self.size] = 0
        self.size -= 1
        self.max_heapify(self.front)
        return popElement


maxHeap = MaxHeap(10)
maxHeap.insert(10)
maxHeap.insert(20)
maxHeap.insert(30)
maxHeap.insert(40)
maxHeap.insert(50)
maxHeap.insert(5)
maxHeap.insert(100)
maxHeap.insert(70)
maxHeap.insert(4)
maxHeap.print_heap()
print(str(maxHeap.heap))
print(maxHeap.extract_max())
print(str(maxHeap.heap))
maxHeap.print_heap()
print(maxHeap.extract_max())
print(str(maxHeap.heap))
maxHeap.print_heap()
