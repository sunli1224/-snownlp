#coding:utf-8
from mysql_cun import mysql_link
from snownlp import SnowNLP
import threading
'''
对京东笔记本品牌购买前100条评论
进行情感分析
数据存储到数据库
'''
class Nlp(threading.Thread):
    def __init__(self,brand):
        threading.Thread.__init__(self)
        self.mysql_cun = mysql_link.mysqlConnect()
        self.base = []
        self.brand = brand
        self.bd = {u"lenvothinkpad":u"联想",u"dellyx":u"戴尔",u"hx":u"华硕"}
        self.base_dict = {"good":0,"middle":0,"bad":0}



    def linkdatabase(self):
        sql = u"select comments from %s"%(self.brand)
        base = self.mysql_cun.find_data(sql)
        for item in base:
            self.base.append(item[0])



    def analyze_comment(self):
        for item in self.base:
            s = SnowNLP(item)
            ds = s.sentiments
            if ds > 0.7:
                self.base_dict["good"] +=1
            if ds < 0.4:
                self.base_dict["bad"] +=1
            if ds <= 0.7 and ds >= 0.4:
                self.base_dict["middle"] +=1

        datas = self.bd[self.brand]
        self.base_dict[u"brand"] = datas
        print self.base_dict


    def ay_cun(self):
        sql = u"insert into ay(good,middle,bad,brand) values(%s,%s,%s,'%s')"%(self.base_dict["good"],self.base_dict["middle"],self.base_dict["bad"],self.base_dict["brand"])
        self.mysql_cun.search_data(sql)



    def run(self):
        self.linkdatabase()
        self.analyze_comment()
        self.ay_cun()



if __name__ == "__main__":
    print u"开始。。。"
    allbrand = [u"lenvothinkpad",u"dellyx",u"hx"]
    for item in allbrand:
        Start = Nlp(item)
        Start.start()
    print u"结束。。。"