#!/usr/local/bin/python
#-*- coding: utf-8 -*-

import hashlib
import requests

from time import strftime, localtime, mktime, strptime, sleep, time
def checking():
    ip = ['10.103.9.108','10.103.9.109','10.108.27.91','10.108.27.92','10.111.5.71','10.111.5.72','10.110.0.96','10.110.0.97','10.109.0.110','10.109.0.111','10.111.5.17','10.111.5.18','10.108.27.117','10.109.0.228','10.110.0.190','10.103.9.18','10.103.9.19'] 
    now = int(time())
    m = hashlib.md5()
    m.update(str(now))
    now_md5 = m.hexdigest()
    srv_down = []
    res = ''
    for d in ip:
        try:
            url = """http://%s/test?t=%s""" % (d,now)
            r = requests.get(url)
            if r.status_code == 200 and r.text == now_md5:
                continue
        except:
            res += d + "   "
    if res != '':
        res += 'stat server 挂了啊亲们'
    return res
