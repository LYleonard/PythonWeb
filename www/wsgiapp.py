# !/usr/bin/env python
#_*_ coding:utf-8 _*_

__author__ = 'LYleonard'

''' A WSGI application entry. '''

import logging; logging.basicConfig(level=logging.INFO)

import os, time
from datetime import datetime

from transwarp import db
from transwarp.web import WSGIApplication, Jinja2TemplateEngine

from config import configs

def datetime_filter(t):
    delta = int(time.time()-t)
    if delta < 60:
        return u'one minute ago'
    if delta < 3600:
        return u'%s minutes ago' % (delta // 60)
    if delta < 7200:
        return u'one hour ago'
    if delta < 86400:
        return u'%s hours ago' % (delta //3600)
    if delta < 604800:
        return u'%s days ago' % (delta // 86400)
    dt = datetime.fromtimestamp(t)
    return u'%年%s月%s日' % (dt.year, dt.month, dt.day)

# init db:
db.create_engine(**configs.db)

# init wsgi app:
wsgi = WSGIApplication(os.path.dirname(os.path.abspath(__file__)))
template_engine = Jinja2TemplateEngine(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))
wsgi.template_engine = template_engine

import urls

wsgi.add_interceptor(urls.user_interceptor)
wsgi.add_interceptor(urls.manage_interceptor)
wsgi.add_module(urls)

if __name__ == '__main__':
    wsgi.run(9000, host='0.0.0.0')
