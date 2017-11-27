#!/usr/bin/python3

import requests

def get_html(url):
    try:
        head={'user-agent':'Mozilla/5.0'}
        params={'wd':'hello'}
        r=requests.get(url,params=params ,timeout=30,headers=head)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except requests.HTTPError:
        return "有异常产生"

if __name__=="__main__":
    url="http://www.baidu.com/s"
    print(get_html(url))
