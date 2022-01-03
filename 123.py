#!/usr/bin/env python
# encoding: utf-8
from flask import Flask,session,redirect,request,render_template
app = Flask(__name__)
app.secret_key = '1sfsdfst'
@app.before_request  # 请求进入视图函数之前加载
def be1():
    print('before_request....1')
@app.before_request
def be2():
    print('before_request....2')
    # return '错误'  # flask 返回的是HTTPRESPONSE对象
@app.before_request
def be3():
    print('before_request....3')
@app.after_request  # 请求视图函数响应客户端之前加载
def af1(args):
    # print(args)  # <Response 5 bytes [200 OK]>
    print('最后一个')
    return args  # 返回的是Response对象
@app.after_request  # 请求视图函数响应客户端之前加载
def af1(args):
    # print(args)  # <Response 5 bytes [200 OK]>
    print('after_request...1')
    return args  # 返回的是Response对象
@app.after_request
def af2(args):
    print('after_request...2')
    return args  # 返回的是Response对象
@app.after_request
def af3(args):
    print('after_request...3')
    return args  # 返回的是Response对象
@app.errorhandler(404)
def error(args):
    print(args)
    return '输出错误页面'
@app.route('/index',endpoint="indexsendpoint")
def index():
    print('我是视图函数')
    return render_template("index.html")
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)