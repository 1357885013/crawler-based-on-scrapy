# -*- coding: utf-8 -*-
from getschool import parse_all
import scrapy
from bs4 import BeautifulSoup
from school.items import SchoolItem
import bs4
import re
# reload(sys)
# sys.setdefaultencoding('utf-8')


class GetallSpider(scrapy.Spider):
    name = 'getall'
    allowed_domains = ['yz.chsi.com.cn', 'baidu.com']
    start_urls = ['http://yz.chsi.com.cn/sch/']

    def parse(self, response):
        if response.url.find("yz.chsi.com.cn") != -1:
            s = BeautifulSoup(response.text, 'html.parser')
            for tr in s.tbody.children:  # 提取表格
                if not isinstance(tr, bs4.element.Tag):
                    continue
                item = SchoolItem()
                i = {}
                tds = tr.find_all('td')
                item['name'] = tds[0].a.text.strip()
                spans = tds[3].find_all('span')
                i['is211'] = ''
                i['is985'] = ''
                try:
                    for ii in range(2):
                        if spans[ii].text == '985':
                            i['is985'] = '985'
                        elif spans[ii].text == '211':
                            i['is211'] = '211'
                except IndexError:
                    pass

                if isinstance(tds[4].i, bs4.element.Tag):
                    i['isGraduate'] = 'GraduateSchool'
                else:
                    i['isGraduate'] = ''
                if isinstance(tds[5].i, bs4.element.Tag):
                    i['isSelfCrossed'] = 'SelfCrossed'
                else:
                    i['isSelfCrossed'] = ''
                item['other'] = i
                yield item

                if item['name'][-2:] in ["大学", "学院"] and item['name'][-3:] not in ["医学院", "科学院"]:
                    url_left = "https://baike.baidu.com/item/"
                    url = url_left + item['name']
                    print("======" + url + "=======\n")
                    yield scrapy.Request(url, callback=self.parse)
                    # 提交当前学校百度百科请求

            ul = response.xpath("//form[@method]/ul")
            try:
                url = re.match(r'(http://[^/]*)/', response.url).group(1) + \
                    ul.xpath("li[last()-1]/a/@href").extract()[0]  # 合成绝对路径
                yield scrapy.Request(url, callback=self.parse)  # 提交下一页请求
            except IndexError:
                pass
        else:
            print("\n get it \n")
            temp = parse_all(response.text)
            item = SchoolItem()
            item['name'] = temp["中文名"]
            item['other'] = temp
            yield item
