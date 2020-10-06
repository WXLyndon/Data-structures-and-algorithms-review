class MyArray:
    def __init__(self):
        self.length = 0
        self.data = []
        
    def get(self, index):
        return self.data[index]

newArray = MyArray()
print(newArray)