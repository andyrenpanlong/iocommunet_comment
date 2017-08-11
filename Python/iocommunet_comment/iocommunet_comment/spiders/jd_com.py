# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from iocommunet_comment.items import commentItem
from pymongo import MongoClient
import json


class jd_com(Spider):
    name = "jd_com"
    start_urls = []

    client = MongoClient('127.0.0.1', 27017)
    db = client.admin
    collection = db.product
    # 查找集合中所有数据
    for item in collection.find():
        print "列表为：", item['link'], item['pid'], item['commentVersion'], item['comment_num']
        comment_total = int(item['comment_num'])
        pages = 0
        if comment_total % 10 == 0:  # 算出评论的页数，一页10条评论
            pages = comment_total/10
        else:
            pages = comment_total/10 + 1
        for page in range(1, pages + 1, 1):
            comment_url = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv" + item['commentVersion'] + "&productId=" + str(item['pid']) + "&score=0&sortType=5&page=" + str(page) + "&pageSize=10&isShadowSku=0&rid=0&fold=1"
            start_urls.append(comment_url)

    print "共计条数", len(start_urls)


    def parse(self, response):
        temp1 = response.body.split('productAttr')
        str = '{"productAttr' + temp1[1][:-2]
        str = str.decode("gbk").encode("utf-8")
        js = json.loads(unicode(str, "utf-8"))
        # print "获取的信息如下", js ,'\n'
        msgData = json.JSONDecoder().decode(str)
        print "解析的信息为：", msgData
        comments = js['comments']  # 该页所有评论
        items = []
        for comment in comments:
            # print "评论如下", comment
            item1 = commentItem()
            item1['all'] = comment
            # item1[''] = comment['']
            # item1['user_name'] = comment['nickname']
            # item1['user_ID'] = comment['id']
            # item1['userProvince'] = comment['userProvince']
            # item1['content'] = comment['content']
            # item1['good_ID'] = comment['referenceId']
            # item1['good_name'] = comment['referenceName']
            # item1['date'] = comment['referenceTime']
            # item1['replyCount'] = comment['replyCount']
            # item1['score'] = comment['score']
            # item1['status'] = comment['status']
            # title = ""
            # if comment.has_key('title'):
            #     item1['title'] = comment['title']
            # item1['title'] = title
            # userRegisterTime = ''
            # if comment.has_key('userRegisterTime'):
            #     item1['userRegisterTime'] = comment['userRegisterTime']
            # item1['userRegisterTime'] = userRegisterTime
            # item1['productColor'] = comment['productColor']
            # item1['productSize'] = comment['productSize']
            # item1['userLevelName'] = comment['userLevelName']
            # item1['isMobile'] = comment['isMobile']
            # item1['days'] = comment['days']
            # tags = ""
            # if comment.has_key('commentTags'):
            #     for i in comment['commentTags']:
            #         tags = tags + i['name'] + " "
            # item1['commentTags'] = tags
            items.append(item1)
        return items