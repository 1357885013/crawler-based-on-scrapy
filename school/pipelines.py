# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

class SchoolPipeline(object):
    def __init__(self):
        self.file=open('school.txt','wb')
        self.ids_seen=set()

    def process_item(self, item, spider):
        if item['name'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.file.write("<{name:^20}>\t<{belong:^16}>\t<{address:^16}>\t<{is985:^3}>\t<{is211:^3}>\t<{isGraduate:^8}>\t<{isSelfCrossed:^11}>\n".format(**item))
            self.ids_seen.add(item['name'])
            return item
