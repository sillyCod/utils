# -*- coding: utf-8 -*-
# @Time    : 2018/7/18 17:40
# @File    : db.py

import pymysql
import traceback
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext import declarative

pymysql.install_as_MySQLdb()

Base = declarative.declarative_base()
params = dict(username="root",
              password="gstianfu",
              host="127.0.0.1",
              db="diff")

engine = create_engine("mysql://{username}:{password}@{host}/{db}".format(**params))

db_session = scoped_session(sessionmaker(engine, autoflush=False, autocommit=False))

Base.query = db_session.query_property()
Base.metadata.create_all(engine)


class Test(Base):
    __tablename__ = 'user'

    id = Column("id", INT, primary_key=True)
    address = Column("address", JSON)


if __name__ == "__main__":
    session = db_session()
    try:
        t = Test(address=dict(city="Peking", district="Chaoyang"))
        session.add(t)
    except Exception as e:
        traceback.print_exc()
        session.roll_back()
    else:
        session.commit()


