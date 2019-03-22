# -*- coding: utf-8 -*-
"""
    @description: 
    @copyright: (c) 2019/3/21 16:29 by Henry.
"""
from contextlib import contextmanager

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy

__author__ = 'Henry'


class SQLAlchemy(_SQLAlchemy):

    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True     # 不会创建base表
    pass


