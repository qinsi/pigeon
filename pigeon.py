#!/usr/bin/python  
# -*- conding:utf-8 -*-  

from bottle import *

@route('/pigeon', methods=['GET', 'POST'])
def pigeon():
    category = request.query.category
    way = request.query.way
    if category == '1':
        content = request.query.content
    if category == '2':
        server = request.query.server
        if server == 'logstat':
            from scripts.logstat import *
            content = checking()

    if content != '':
        #mail
        if way == '1':
            user = request.query.user
            passwd = request.query.passwd

        #dingtalk
        if way == '2':
            token = request.query.token
            from send.dingtalk import *
            sending(token,content)
    return '200 OK'

run(host='0.0.0.0', port=7081)
