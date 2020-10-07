class MyArray:
    def __init__(self):
        self.length = 0
        self.data = []
        
    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data.append(item)
        self.length += 1
        return self.length

    def pop(self):
        item = self.data[-1]
        self.data = self.data[:self.length-1] # python list's index is left closed right open
        self.length -= 1
        return item
    
    def delete(self, index):
        item = self.data[index]
        self.shiftItems(index)
        return item
    
    def shiftItems(self, index):
        for i in range(index, self.length-1):
            self.data[i] = self.data[i + 1]
        self.data = self.data[:self.length-1]
        self.length -= 1

newArray = MyArray()
newArray.push('hi')
newArray.push('you')
newArray.push('!')
newArray.delete(1)
print(newArray.data, newArray.length)