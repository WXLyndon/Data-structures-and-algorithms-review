# Create a function that reverses a string:
# 'Hi My name is Lyndon' should be:
# 'nodnyL si eman yM iH'

def reverse(str):
    # error checking
    if type(str) != str:
        return "The input is not a string."

    rev_str = ''
    for index in range(len(str)):
        rev_str += str[len(str) - 1 - index]
    return rev_str

str = 'Hi My name is Lyndon'
print(reverse(str))