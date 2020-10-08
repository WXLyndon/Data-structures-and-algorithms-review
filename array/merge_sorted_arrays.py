# input:[0,3,4,31], [4,6,30]
# output: [0,3,4,4,6,30,31]

def merge(arr1, arr2):
    mergeArr = []
    
    # Check if arr1 or arr2 is empty
    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1

    arr1_index = 0
    arr2_index = 0

    while (arr1_index < len(arr1)) or (arr2_index < len(arr2)): # any input arr is not entirely checked
        # arr1 is not entirely checked; and arr2 is entirely checked, or current arr1 item is less than current arr2 item.
        if (arr1_index < len(arr1)) and ((arr2_index >= len(arr2)) or (arr1[arr1_index] < arr2[arr2_index])):
            mergeArr.append(arr1[arr1_index])
            arr1_index += 1
        else:
             mergeArr.append(arr2[arr2_index])
             arr2_index += 1
    
    return mergeArr


# print(merge([0,3,4,31],[4,6,30]))

print(merge([4,6,30],[0,3,4,31]))