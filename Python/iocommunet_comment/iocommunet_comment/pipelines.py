# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient

class IocommunetCommentPipeline(object):
    def process_item(self, item, spider):
        client = MongoClient('127.0.0.1', 27017)
        db = client.admin
        data = {}
        # data['user_name'] = item['user_name']
        # data['user_ID'] = item['user_ID']
        # data['userProvince'] = item['userProvince']
        # data['content'] = item['content']
        # data['good_ID'] = item['good_ID']
        # data['good_name'] = item['good_name']
        # data['date'] = item['date']
        # data['replyCount'] = item['replyCount']
        # data['score'] = item['score']
        # data['status'] = item['status']
        # data['title'] = item['title']
        # data['userRegisterTime'] = item['userRegisterTime']
        # data['productColor'] = item['productColor']
        # data['productSize'] = item['productSize']
        data2 = item['all']
        db.comment.insert(data2)
        print "yes"

