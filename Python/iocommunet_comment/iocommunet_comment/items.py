# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field

class IocommunetCommentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class commentItem(Item):
    user_name = Field()  # 评论用户的名字
    user_ID = Field()  # 评论用户的ID
    userProvince = Field()  # 评论用户来自的地区
    content = Field()  # 评论内容
    good_ID = Field()  # 评论的商品ID
    good_name = Field()  # 评论的商品名字
    date = Field()  # 评论时间
    replyCount = Field()  # 回复数
    score = Field()  # 评分
    status = Field()  # 状态
    title = Field()
    userLevelId = Field()
    userRegisterTime = Field()  # 用户注册时间
    productColor = Field()  # 商品颜色
    productSize = Field()  # 商品大小
    userLevelName = Field()  # 银牌会员，钻石会员等
    userClientShow = Field()  # 来自什么 比如来自京东客户端
    isMobile = Field()  # 是否来自手机
    days = Field()  # 天数
    all = Field() #全部数据
    commentTags = Field()  # 标签
