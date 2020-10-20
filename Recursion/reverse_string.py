def reverseStringRecursive(string):
    if len(string) == 0:
        return string
    return reverseStringRecursive(string[1:]) + string[0]


def reverseStringIterative(string):
    reverse = ''
    for i in range(len(string)):
        reverse += string[len(string) - i - 1]
    return reverse


print(reverseStringIterative('Donald Trump is stupid'))
print(reverseStringRecursive('Donald Trump is stupid'))
