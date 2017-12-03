# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import codecs
import json


class SchoolPipeline(object):
    data = {}

    def __init__(self):
        pass

    def process_item(self, item, spider):
        try:
            SchoolPipeline.data[item['name']]
        except KeyError:
            SchoolPipeline.data[item['name']] = item['other']
            return item
        SchoolPipeline.data[item['name']].update(item['other'])
        return item

    def __del__(self):
        string = json.dumps(SchoolPipeline.data, indent=4, separators=(',', ': '))
        string = string.encode()
        string = string.decode("unicode-escape")
        f = codecs.open('allSchool.txt', 'w', 'utf-8')
        f.write(string)
        f.close()
