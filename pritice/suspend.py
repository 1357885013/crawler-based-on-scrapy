#!/usr/bin/python3

import time

a={1:"suspend 暂停100ms",2:"suspend 暂停完成"}
#for key,value in dict.items(a):
for key,value in a.items():
    print(key,":",value,end="\n")
    time.sleep(1)   #可以是小数，单位是秒

