# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SchoolItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field()
    address=scrapy.Field()
    belong=scrapy.Field()
    is985=scrapy.Field()
    is211=scrapy.Field()
    isGraduate=scrapy.Field()
    isSelfCrossed=scrapy.Field()
