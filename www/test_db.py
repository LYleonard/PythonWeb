#! /usr/bin/env python
# _*_ soding: utf-8 _*_

__author__ = 'LYleoanrd'

from models import User
from transwarp import db

db.create_engine(user='root', password='243015', database='awesome')

u = User(name='Test', email='test@example.com', password='1234567890', image='about:blank')

# Test insert data
u.insert()
print 'new user id:', u.id

# Test query
u1 = User.find_first('where email=?', 'test@example.com')
print 'find user\'s name:', u1.name

#  Test delete
u1.delete()
u2 = User.find_first('where email=?', 'test@example.com')
print 'find user:',u2