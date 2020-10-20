def bubbleSort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
bubbleSort(numbers)
print(numbers)