import time

def fibonacci(n):
    if (n < 2):
        return n

    return fibonacci(n-1) + fibonacci(n-2)

cache = {}
def fibonacciDP(n):
    if n in cache:
        return cache[n]
    if n < 2:
        return n
    else:
        cache[n] = fibonacciDP(n-1) + fibonacciDP(n-2)
        return cache[n]

start1 = time.clock()
print(fibonacci(30))
end1 = time.clock()
print(end1 - start1)

start2 = time.clock()
print(fibonacciDP(30))
end2 = time.clock()
print(end2 - start2)