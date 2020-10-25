def maxHeapify(array, size, i):
    left = 2 * i + 1
    right = 2 * i + 2
    maximum = i

    if left < size and array[i] < array[left]:
        maximum = left

    if right < size and array[maximum] < array[right]:
        maximum = right

    if maximum != i:
        array[i], array[maximum] = array[maximum], array[i]
        maxHeapify(array, size, maximum)


def heapSort(array):
    size = len(array)

    for i in range(size, -1, -1):
        maxHeapify(array, size, i)

    for i in range(size-1, 0, -1):
        array[i], array[0] = array[0], array[i] # array[0] is the maximum in the current loop
        maxHeapify(array, i, 0)


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
heapSort(numbers)
print(numbers)
