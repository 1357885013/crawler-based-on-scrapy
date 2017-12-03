#!/usr/bin/python3
import re
import json
from lxml import etree
import codecs


def x_to_h(a):
    "十六进制到十进制"
    num = ['0', '1', '2', '3', '4', '5', '6', '7',
           '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    ans = ""
    while a > 15:
        ans = num[int(a % 16)] + ans
        a /= 16
    if int(a) != 0:
        ans = num[int(a)] + ans
    return ans


def get_td2(html, end):
    "得到下面表格的东西"
    t = etree.HTML(html)
    temp = t.xpath("//div[@class='basic-info cmn-clearfix']/dl")
    keys = temp[0].xpath("./dt") + temp[1].xpath("./dt")
    values = temp[0].xpath("./dd") + temp[1].xpath("./dd")
    for i in range(0, len(keys) - 1):
        key = keys[i].xpath("./text()")[0]
        key = re.sub(r"\s", "", key)
        value = get_str_2(values[i])
        # print(key, ":", value)
        end[key] = value
        # print(type(values[i]))


def get_td(html, end):
    "得到上面表格的东西"
    t = etree.HTML(html)
    temp = t.xpath("//div[@class='baseBox']/div")
    temp = temp[0].xpath("./dl") + temp[1].xpath("./dl")
    for dl in temp:
        key = dl.xpath("./dt/text()")[0]
        key = re.sub(r"\s", "", key)    # 去空格
        value = get_str(dl.xpath("./dd"))
        # print(key, ":", value)
        end[key] = value


def get_str_2(t_oo):
        "得到下面表格里的元素里的文字"
        string = etree.tostring(t_oo)
        string = string.decode('UTF-8', 'strict')
        # print("原文:\n" + string)
        string = re.sub(r"<.*?>", "", string)
        string = re.sub(r"\[\d*\]", "", string)
        string = re.sub(r"\n", "", string)
        re_a = re.findall(r"&#.*?;", string)
        for i in re_a:
            o = x_to_h(int(i[2:-1]))
            if len(o) < 4:
                o = '0' * (4 - len(o)) + o
            string = string.replace(i, "\\u" + o)
        string = string.encode()
        string = string.decode('unicode-escape')
        return string


def get_str(t_o):
    "得到上面表格里的元素里的文字"
    text = ""
    for t_oo in t_o:
        string = etree.tostring(t_oo)
        string = string.decode('UTF-8', 'strict')
        # print("原文:\n" + string)
        string = re.sub(r"<.*?>", "", string)
        string = re.sub(r"\[\d*\]", "", string)
        string = re.sub(r"\n", "", string)
        re_a = re.findall(r"&#.*?;", string)
        for i in re_a:
            o = x_to_h(int(i[2:-1]))
            if len(o) < 4:
                o = '0' * (4 - len(o)) + o
            string = string.replace(i, "\\u" + o)
        string = string.encode()
        string = string.decode('unicode-escape')
        text += string
    return text


def parse_all(html):
    end = {}
    get_td2(html, end)
    get_td(html, end)
    return end


def get_str_fail(t_o):
    "遍历所有标签和文字 得到所有文字"
    text = ""  # 但是所有标签外文字会在左边，标签内会在右边，字的顺序会乱
    for t in t_o:
        tt = t.xpath("./text()")
        for i in tt:
            text += i.strip()

        if isinstance(t.xpath("./*"), list):
            text += get_str(t.xpath("./*"))
    return text
