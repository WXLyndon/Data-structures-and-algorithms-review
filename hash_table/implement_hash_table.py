# Implementation of the hash table
class HashTable:

    def __init__(self, size):
        self.data = [None] * size
        self.size = size

    def __hash(self, key):  # private method
        hash = 0
        for i in range(len(key)):
            # ord():Return the Unicode code point for a one-character string.
            hash = (hash + ord(key[i]) * i) % self.size
        return hash

    def set(self, key, value):
        address = self.__hash(key)

        if (self.data[address] == None):  # no hash collision, first access to this address
            self.data[address] = []

        self.data[address].append([key, value])
        return self.data

    def get(self, key):
        address = self.__hash(key)
        currBucket = self.data[address]

        if currBucket != None:
            for item in currBucket:
                if item[0] == key:
                    return item[1]

    # Get all the keys in the HashTable object
    def keys(self):
        keysArr = []

        for bucket in self.data:
            if bucket != None:
                if len(bucket) > 1:  # has hash collision
                    for item in bucket:
                        keysArr.append(item[0])
                else:  # no hash collision
                    keysArr.append(bucket[0][0])

        return keysArr


hashTable = HashTable(2)
hashTable.set('grapes', 5000)
hashTable.set('apples', 10000)
print(hashTable.set('oranges', 2))
# print(hashTable.get('apples'))
print(hashTable.keys())
