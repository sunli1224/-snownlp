#coding:utf-8
import os
'''
遵守MTV原则
'''

web = {
    'debug':True,#debug可以检测代码更新是会重新启动服务器，而且代码有错时，会提示错误信息
    'template_path':os.path.dirname(__file__) + '/template',#插入模板的路径地址
    'static_path': os.path.join(os.path.dirname(__file__), "static"),#加入静态文件路径
    "cookie_secret": 'test-secret-sunli-bblike-cn',#设置cookie的加密字段
}