# Google Question
# Given an array = [2,5,1,2,3,5,1,2,4]:
# It should return 2

# Given an array = [2,1,1,2,3,5,1,2,4]:
# It should return 1

# Given an array = [2,3,4,5]:
# It should return undefined

def first_recurr_char(arr):
    dict = {}

    for char in arr:
        if char in dict:
            return char
        dict[char] = 1
    return None
 
arr1 = [2,5,1,2,3,5,1,2,4]
print(first_recurr_char(arr1))
arr2 = [2,1,1,2,3,5,1,2,4]
print(first_recurr_char(arr2))
arr3 = [2,3,4,5]
print(first_recurr_char(arr3))