#!/usr/bin/python3

def x_to_h(a):
    num=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    ans=""
    while a>15:
        ans=num[int(a%16)]+ans
        a/=16
        print(a)
    if int(a)!=0:
        ans=num[int(a)]+ans
    return ans
print(x_to_h(int(input('input:'))))
