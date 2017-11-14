# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

class SchoolPipeline(object):
    def __init__(self):
        self.file=open('school.txt','ab')

    def process_item(self, item, spider):
        if item['name'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
            return item
#self.file.write("{:^20}\t{:^16}\t{:^16}\t{:^3}\t{:^3}\t{:^4}\t{:^3}\t".format(item))
        self.file.write("hello world!")
        
        self.ids_seen.add(item['name'])
        return item
