import random


def quickSort(array, left, right):
    if left < right:
        partitionIndex = randomPartion(array, left, right)
        # partitionIndex = partition(array, left, right)
        quickSort(array, left, partitionIndex)
        quickSort(array, partitionIndex + 1, right)
    else:
        return


def partition(array, left, right):
    i = left - 1
    for j in range(left, right):
        if array[j] <= array[right]:
            i += 1
            swap(array, i, j)
    swap(array, i+1, right)
    return i


def randomPartion(array, left, right):
    i = random.randint(left, right)
    swap(array, i, right)
    return partition(array, left, right)


def swap(array, firstIndex, secondIndex):
    array[firstIndex], array[secondIndex] = array[secondIndex], array[firstIndex]


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
quickSort(numbers, 0, len(numbers)-1)
print(numbers)
