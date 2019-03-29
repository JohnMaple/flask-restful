# -*- coding: utf-8 -*-
"""
    @description: 初始化项目，加载配置项，注册蓝图、数据库等
"""
from .app import Flask

from app.models.base import db
from app import models

__author__ = 'Henry'


def register_blueprint(app):
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def register_plugins(app):
    # 注册模型
    db.init_app(app)


def create_app():
    app = Flask(__name__)

    # 加载配置项
    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.settings')

    # 注册蓝图
    register_blueprint(app)

    # 注册插件
    register_plugins(app)

    return app

