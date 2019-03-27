# -*- coding: utf-8 -*-
"""
    @description: 客户端（包括用户，第三方平台等）
    @copyright: (c) 2019/3/27 16:08 by Henry.
"""
from app.libs.redprint import Redprint


__author__ = 'Henry'


api = Redprint('client')


@api.route('/register')
def create_client():
    # 参数校验
    pass




