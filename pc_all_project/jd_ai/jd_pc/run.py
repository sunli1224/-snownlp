#coding:utf-8
import tornado.httpserver
import tornado.web
import tornado.ioloop
import settings
import tornado.options
from tornado.options import define, options
from mysql_cun import mysql_link
import json

define("port", default=9000, help="run on the given port", type=int)

class home(tornado.web.RequestHandler):
    def get(self, *args):
        sql = u'select * from ay'
        datas = mysql_link.mysqlConnect().find_data(sql)
        BaoOne =  datas[0][4]
        Baotwo =  datas[1][4]
        Baothree = datas[2][4]
        self.render('home.html',BaoOne=BaoOne,Baotwo=Baotwo,Baothree=Baothree)

    def post(self, *args, **kwargs):
        self.render('home.html')

class text(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('text.html')
    def post(self, *args, **kwargs):
        # start = self.get_argument('start')
        # if start == 1:
        sql = u'select * from ay'
        datas = mysql_link.mysqlConnect().find_data(sql)
        # for item in datas:
        BaoOne = [datas[0][1], datas[0][2], datas[0][3], datas[0][4]]
        Baotwo = [datas[1][1], datas[1][2], datas[1][3], datas[1][4]]
        Baothree = [datas[2][1], datas[2][2], datas[2][3], datas[2][4]]
        # self.finish([BaoOne,Baotwo,Baothree])
        # self.write(json.dumps({"baoone":BaoOne}))
        self.finish(json.dumps({"a1":datas[0][1],"a2":datas[0][2],"a3":datas[0][2],"b1":datas[1][1],"b2":datas[1][2],"b3":datas[1][3],"c1":datas[2][1],"c2":datas[2][2],"c3":datas[2][3]}))
        # self.render('home.html',BaoOne=BaoOne,Baotwo=Baotwo,Baothree=Baothree)



if __name__ == '__main__':
    app = tornado.web.Application([
        (r"/home/(.*)", home),
        (r"/text/(.*)", text)
    ],**settings.web)

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()