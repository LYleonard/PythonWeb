#! /usr/bin/env python
# _*_ soding: utf-8 _*_

__author__ = 'LYleoanrd'

from models import User, Blog, Comment
from transwarp import db

db.create_engine(user='www-data', password='www-data', database='awesome')

u = User(name='Test', email='test@example.com', password='12345678', image='about:blank')

u.insert()

print 'new user id:', u.id

u1 = User.find_first('where email=?', 'test@example.com')
print 'find user\'s name:', u1.name

u1.delete()

u2 = User.find_first('where email=?', 'test@example.com')
print 'find user:',u2