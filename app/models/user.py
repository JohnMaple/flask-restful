# -*- coding: utf-8 -*-
"""
    @description: 
    @copyright: (c) 2019/3/27 16:58 by Henry.
"""
from sqlalchemy import Column, Integer, String, SmallInteger
from werkzeug.security import generate_password_hash

from app.models.base import Base, db

__author__ = 'Henry'


class User(Base):
    id = Column(Integer, primary_key=True, comment='id')
    nickname = Column(String(24), nullable=False, comment='昵称')
    email = Column(String(24), unique=True, nullable=False, comment='邮箱')
    auth = Column(SmallInteger, default=1, comment='权限，超级管理员或普通用户')
    _password = Column('password', String(128), nullable=False, comment='密码')

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    @staticmethod
    def register_by_email(nickname, account, secret):
        with db.auto_commit():
            user = User()
            user.nickname = nickname
            user.email = account
            user.password = secret
            db.session.add(user)



