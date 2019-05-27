#coding:utf-8
import requests
import re
import json
from mysql_cun import mysql_link
import threading
'''
多线程爬取
解析json文件
内容存放数据库
京东商品
各类品牌笔记本的前一百条评论
华硕; https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv4958&productId=100000208933&score=0&sortType=5&page=%s&pageSize=10&isShadowSku=0&fold=1
thinkpad: https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv19195&productId=6072622&score=0&sortType=5&page=%s&pageSize=10&isShadowSku=0&rid=0&fold=1
dell: https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv9806&productId=7555189&score=0&sortType=5&page=%s&pageSize=10&isShadowSku=0&rid=0&fold=1
'''
class Comment(threading.Thread):
    def __init__(self,ids):
        threading.Thread.__init__(self)
        self.url = u" https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv4958&productId=100000208933&score=0&sortType=5&page=%s&pageSize=10&isShadowSku=0&fold=1"%(ids)
        self.base = []
        self.mysql_cun = mysql_link.mysqlConnect()

    def jday(self):
        page = requests.get(self.url).text
        # print page
        data = re.findall(r"{.*}",page)[0]
        # print data
        datajosn = json.loads(data).get(u"comments")
        # print datajosn.get(u"comments")[3].get(u"content")
        for item in datajosn:
            self.base.append(item.get(u"content"))


    def storage(self):
        for item in self.base:
            sql = u"insert into Hx(comments) values('%s')"%(item)
            self.mysql_cun.search_data(sql)



    def run(self):
        self.jday()
        self.storage()




if __name__ == "__main__":
    print u"开始。。。"
    count =10
    for i in range(0,count):
        start = Comment(i)
        start.start()
    print u"结束。。。"