# -*- coding: utf-8 -*-
"""
    @description: 
    @copyright: (c) 2019/3/27 16:10 by Henry.
"""
from enum import Enum

__author__ = 'Henry'


class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101

    # 微信小程序
    USER_MINA = 200

    # 微信公众号
    USER_WX = 201


