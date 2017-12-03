#!/usr/bin/python3


def fib1(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib1(n - 1) + fib1(n - 2)


def fib2(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


def fib3(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b, n = b, a + b, n + 1


print(fib1(10))
for i in fib3(10):
    print(i)
