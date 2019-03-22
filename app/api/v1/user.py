# -*- coding: utf-8 -*-
"""
    @description: 
    @copyright: (c) 2019/3/21 16:47 by Henry.
"""
from app.libs.redprint import Redprint

__author__ = 'Henry'


api = Redprint('user')


@api.route('/get')
def get_user():
    return 'i am henry'


