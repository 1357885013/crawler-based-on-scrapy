#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
import bs4

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

def get_td(ulist,html):
    s=BeautifulSoup(html,'html.parser')
    for tr in s.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds=tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[3].string])

def out_td(ulist,num):
    temp="{:^10}\t{:^15}\t{:^10}"
    print(temp.format("排名","学校","总分",chr(12288)))
    print('-'*50)
    for i in range(num):
        u=ulist[i]
        print(temp.format(u[0],u[1],u[2],chr(12288)))

def main():
    url="http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
    
    ulist=[]
    html=get_html(url)
    get_td(ulist,html)
    out_td(ulist,20)
    
main()
