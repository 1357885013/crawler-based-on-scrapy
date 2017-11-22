#!/usr/bin/python3

num=[1000000,600000,400000,200000,100000,0]
precent=[0.01,0.015,0.03,0.05,0.075,0.1]

money=int(input('净利润：'))
r=0
for i in range(6):
    if money>num[i]:
        r+=(money-num[i])*precent[i]
        money=num[i]
print(r)
    
