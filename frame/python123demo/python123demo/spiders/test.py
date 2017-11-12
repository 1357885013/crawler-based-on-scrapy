# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['baidu']
    start_urls = ['http://baidu/']

    def parse(self, response):
        pass
