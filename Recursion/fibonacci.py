def fibonacciIterative(index):
    if index == 0:
        return 0
    if index == 1:
        return 1
    fib1 = 0
    fib2 = 1
    for i in range(2, index + 1):
        ans = fib1 + fib2
        fib1 = fib2
        fib2 = ans
    return ans

def fibonacciRecuresive(index):
    if index == 0:
        return 0
    if index == 1:
        return 1
    return fibonacciRecuresive(index - 1) + fibonacciRecuresive(index - 2)

print(fibonacciRecuresive(10))
print(fibonacciIterative(10))