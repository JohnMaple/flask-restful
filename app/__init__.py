# -*- coding: utf-8 -*-
"""
    @description: 初始化项目，加载配置项，注册蓝图、数据库等
    @copyright: (c) 2019/3/21 14:16 by Henry.
"""
from flask import Flask

from app.models.base import db

__author__ = 'Henry'


def register_blueprint(app):
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def create_app():
    app = Flask(__name__)

    # 加载配置项
    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.settings')

    # 注册数据模型
    db.init_app(app)

    # 注册蓝图
    register_blueprint(app)

    return app

