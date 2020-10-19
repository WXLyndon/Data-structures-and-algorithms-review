def findFincotriaRecursive(num):
    if num == 1 or num == 0:
        return 1
    return num * findFincotriaRecursive(num - 1)


def findFincotriaIterative(num):
    if num == 0:
        return 1
    ans = 1
    for i in range(1, num + 1):
        ans *= num + 1 - i
    return ans


print(findFincotriaRecursive(0))
print(findFincotriaRecursive(10))
print(findFincotriaIterative(0))
print(findFincotriaIterative(10))
