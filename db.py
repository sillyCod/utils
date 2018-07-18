# -*- coding: utf-8 -*-
# @Time    : 2018/7/18 17:40
# @File    : db.py

import pymysql

from sqlalchemy import *
from sqlalchemy.ext import declarative

pymysql.install_as_MySQLdb()

Base = declarative.declarative_base()

engine = create_engine("mysql://root:gstianfu@127.0.0.1/diff")

Base.metadata.create_all(engine)


class Test():
    __tablename__ = 'user'

    id = Column(Integer, column='id')
    address = Column(JSON, column='address')

