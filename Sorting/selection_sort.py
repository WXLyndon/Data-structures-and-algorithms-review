def selectionSort(array):
    for i in range(len(array)):
        smallest = array[i]
        smallest_index = i
        for j in range(i+1, len(array)):
            if array[j] < smallest:
                smallest = array[j]
                smallest_index = j
        array[i], array[smallest_index] = smallest,  array[i]

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
selectionSort(numbers)
print(numbers)
