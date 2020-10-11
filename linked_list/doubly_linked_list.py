# Implementation of the doubly linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        string = ''
        node = self.head

        while node is not None:
            if node.next is not None:
                string += str(node.value) + '-->'
            else:
                string += str(node.value)
            node = node.next
        return string

    def doubly_linked_backwards_str(self):
        string = ''
        node = self.tail

        while node is not None:
            if node.prev is not None:
                string += str(node.value) + '-->'
            else:
                string += str(node.value)
            node = node.prev
        return string


    def append(self, value):
        node = Node(value)
        if self.head == None:  # empty linked list
            self.head = node
            self.tail = node
        else:  # not empty
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1

    def prepend(self, value):
        node = Node(value)
        node.next = self.head
        self.head.prev = node
        self.head = node
        self.length += 1

    def insert(self, index, value):
        if index >= self.length:  # insert to the end
            if index > self.length:
                print(
                    'The input index is out of range, the node will be appended to the end.')
            self.append(value)
            return
        if index == 0:  # insert to the start
            self.prepend(value)
            return
        node = Node(value)
        current = self.head
        for i in range(index - 1):  # iterate the linked list
            # in the last loop, current points to the node just before the index node
            current = current.next
        node.next = current.next
        node.prev = current
        current.next.prev = node
        current.next = node
        self.length += 1


    def remove(self, index):
        if self.length == 0:
            raise Exception("The linked list is empty, nothing can be removed.")
        if index >= self.length:
            raise IndexError("Input index out of range")
        if index == 0:  # remove the head node
            if self.length == 1:
                self.head = None
                self.tail = None
            elif self.length == 2:
                self.head = self.head.next
                self.tail = self.head
                self.head.prev = None
            else:
                self.head = self.head.next
                self.head.prev = None
            self.length -= 1
            return
        current = self.head
        for i in range(index - 1):  # iterate the linked list
            # in the last loop, current points to the node just before the index node
            current = current.next
        current.next = current.next.next
        current.next.prev = current
        self.length -= 1
        if current.next == None:
            self.tail = current


myLinkedList = DoublyLinkedList()
myLinkedList.append(1)
myLinkedList.append(2)
myLinkedList.prepend(9)
myLinkedList.insert(3, 4)
myLinkedList.insert(2, 5)
myLinkedList.remove(3)
print(str(myLinkedList))
print(myLinkedList.doubly_linked_backwards_str())