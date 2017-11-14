# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from school.items import SchoolItem
import bs4
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



class GetallSpider(scrapy.Spider):
    name = 'getall'
    allowed_domains = ['yz.chsi.com.cn']
    start_urls = ['http://yz.chsi.com.cn/sch/']
    hasPri=0
    def parse(self, response):
        print("\n\n")
#from scrapy.shell import inspect_response      #shell 调试
#inspect_response(response, self)
        for tr in response.xpath("//table/tbody/tr"):  #提取表格
            i=SchoolItem()
            tds=tr.xpath("td")
            print(type(tds))
            i['name']=tds[1].xpath("text()")
            i['address']=tds[2].xpath("text()")
            i['belong']=tds[3].xpath("text()")
            print("1\n")
            i['is985']= tds[4].xpath("span[1]/text()")
            print("2\n")
            i['is211']= tds[4].xpath("span[2]/text()")
            if self.hasPri==0:
                print(i)
                self.hasPri=1
            yield i

        forms=s.find('form')
        lis=forms[2].children.li
        if lis[-2].a.attrs['href'] !='':
            url=response.urljoin(response.url,lis[-2].a.attrs['href'])#合成绝对路径
            yield scrapy.repuest(url,callback=self.parse)   #提交下一页请求
