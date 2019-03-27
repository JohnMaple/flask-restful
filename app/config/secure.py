# -*- coding: utf-8 -*-
"""
    @description: 环境配置
    @copyright: (c) 2019/3/21 14:53 by Henry.
"""

__author__ = 'Henry'

DEBUG = True

# SCERET_KEY = os.urandom(24)   # 适合开发使用
SECRET_KEY = 'E\xdb/\xccH\xaf\x98q\xfc\xbc`\xec\xedw \xe7H\xa9{?\xbe(@\xa4'

SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:root@localhost:3306/flask_restful'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_TEARDOWN = True


