#!/usr/bin/python3

import requests
import os

def get_html(url):
    try:
        path="/home/liujijiang/python/"
        head={'user-agent':'Mozilla/5.0'}
        r=requests.get(url,timeout=30,headers=head)
        r.raise_for_status()
        print(os.getcwd())
        os.chdir(path)
        with open('catfd.jpg','wb') as f:
            f.write(r.content)
        return '成功采集'
    except requests.HTTPError:
        return "有异常产生"

if __name__=="__main__":
    url="http://img.hb.aicdn.com/29cd691f078d32e40a743bcf35faf7eddd3750d01165a4-WFqKgn_fw658"
    print(get_html(url))
