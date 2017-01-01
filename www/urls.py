#!/usr/bin/env python
#_*_ coding: utf-8 _*_
__author__ = 'LYleonard'

import logging
from transwarp.web import get, view
from models import User,Blog, Comment

@view('test_users.html')
@get('/')
def test_users():
    users = User.find_all()
    return dict(users = users)