#!/usr/bin/python3
import re
from bs4 import BeautifulSoup
from lxml import etree
import requests
import bs4

def x_to_h(a):
    num=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    ans=""
    while a>15:
        ans=num[int(a%16)]+ans
        a/=16
    if int(a)!=0:
        ans=num[int(a)]+ans
    return ans

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

def get_td2(ulist,html):
    t=etree.HTML(html)
    print(type(t))
    temp=t.xpath("//div[@class='basic-info cmn-clearfix']/dl")
    temp=[temp[0],temp[1]]
    keys=temp[0].xpath("./dt")+temp[1].xpath("./dt")
    values=temp[0].xpath("./dd")+temp[1].xpath("./dd")
    for i in range(0,len(keys)-1):
        print(keys[i].xpath("./text()")," : ",get_str_2(values[i]))
#    print(get_str_2(temp[3]))

def get_td(ulist,html):
    t=etree.HTML(html)
    print(type(t))
    temp=t.xpath("//div[@class='baseBox']/div")
    temp=temp[0].xpath("./dl")+temp[1].xpath("./dl")
    for dl in temp:
        print(dl.xpath("./dt/text()")," : ",get_str_2(dl.xpath("./dd")))
#    print(get_str_2(temp[3]))

def get_str_2(t_o):
    text=""
    for t_oo in t_o:
        string=etree.tostring(t_oo)
        print(string)
        string=string.decode('UTF-8','strict')
        re_a=re.findall(r"&#.*?;",string)
        for i in re_a:
            o=x_to_h(int(i[2:-1]))
            if len(o)<4:
                o='0'*(4-len(o))+o
            string=string.replace(i,"\\u"+o)
        string=string.encode()
        string=string.decode('unicode-escape')
        string=re.sub(r"<.*?>","",string)
        string=re.sub(r"\n","",string)
        text+=string
    return text

def get_str(t_o): #遍历所有标签和文字 得到所有文字
    text=""       #但是所有标签外文字会在左边，标签内会在右边，字的顺序会乱
    for t in t_o:
        tt=t.xpath("./text()")
        for i in tt:
           text+=i.strip() 
        
        if isinstance(t.xpath("./*"),list):
            text+=get_str(t.xpath("./*"))
    return text
        
def main():
    url="https://baike.baidu.com/item/清华大学"
    
    ulist=[]
#   html=get_html(url)
    f=open('baike.html','r')
    html=f.read()
    get_td(ulist,html)
    get_td2(ulist,html)
    
main()
