#!/usr/bin/python3
import requests
import codecs


url = "https://baike.baidu.com/item/武汉大学"
try:
    head = {'user-agent': 'Mozilla/5.0'}
    r = requests.get(url, timeout=30, headers=head)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    # print(r.text)
except requests.HTTPError:
    print("有异常产生")
f = codecs.open('baike.html', 'w', 'utf-8')
f.write(r.text)
f.close()
