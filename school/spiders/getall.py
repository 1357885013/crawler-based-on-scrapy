# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from school.items import SchoolItem
import bs4
import sys
import re
reload(sys)
sys.setdefaultencoding('utf-8')



class GetallSpider(scrapy.Spider):
    name = 'getall'
    allowed_domains = ['yz.chsi.com.cn']
    start_urls = ['http://yz.chsi.com.cn/sch/']

    def parse(self, response):
        s=BeautifulSoup(response.text,'html.parser')
        print("\n\n")
#from scrapy.shell import inspect_response      #shell 调试
#inspect_response(response, self)
        for tr in s.tbody.children:  #提取表格
            if isinstance(tr,bs4.element.Tag) == False:
                continue
            i=SchoolItem()
            tds=tr.find_all('td')
            i['name']=tds[0].a.text.strip()
            i['address']=tds[1].text.strip() 
            i['belong']=tds[2].text.strip()
            spans=tds[3].find_all('span')
            i['is211']=''
            i['is985']=''
            try:
                for ii in range(2):
                    if spans[ii].text=='985':
                        i['is985']='985'
                    elif spans[ii].text=='211':
                        i['is211']='211'
            except IndexError:
                pass

            if isinstance(tds[4].i,bs4.element.Tag):
                i['isGraduate']='GraduateSchool'
            else:
                i['isGraduate']=''
            if isinstance(tds[5].i,bs4.element.Tag):
                i['isSelfCrossed']='SelfCrossed'
            else:
                i['isSelfCrossed']=''
            yield i

        ul=response.xpath("//form[@method]/ul")
        try:
            url=re.match(r'(http://[^/]*)/',response.url).group(1)+ul.xpath("li[last()-1]/a/@href").extract()[0]#合成绝对路径
            yield scrapy.Request(url,callback=self.parse)   #提交下一页请求
        except IndexError:
            pass
