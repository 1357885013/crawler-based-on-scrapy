#!/usr/bin/python3
import requests
import os
from lxml import etree


url="https://baike.baidu.com/item/清华大学"
try:
    head={'user-agent':'Mozilla/5.0'}
    r=requests.get(url,timeout=30,headers=head)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
except requests.HTTPError:
    print("有异常产生")
f=open('baike.html','w')
f.write(r.text)
f.close()
