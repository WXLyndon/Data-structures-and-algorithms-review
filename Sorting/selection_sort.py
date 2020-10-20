def selectionSort(array):
    for i in range(len(array)):
        smallest = array[i]
        smallestIndex = i
        for j in range(i+1, len(array)):
            if array[j] < smallest:
                smallest = array[j]
                smallestIndex = j
        array[i], array[smallestIndex] = smallest,  array[i]

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
selectionSort(numbers)
print(numbers)
