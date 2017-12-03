#!/usr/bin/python3
# the different way to copy list

a = [1, 2, 3]


def way1(a):
    b = a[:]
    return b


def way2(a):
    b = []
    for i in range(3):
        b.append(a[i])
    return b


def way3(a):
    b = [i for i in a]
    return b


def way4(a):
    b = []
    for i in a:
        b.append(i)
    return b


def way5(a):
    b = []
    for i in range(len(a)):
        b.append(a[i])
    return b


def way6(a):
    return a.copy()


print(way6(a))
