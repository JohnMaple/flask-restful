# -*- coding: utf-8 -*-
"""
    @description: 
    @copyright: (c) 2019/3/21 16:47 by Henry.
"""
from app.libs.redprint import Redprint

__author__ = 'Henry'

api = Redprint('book')


@api.route('', methods=['GET'])
def get_book():
    return 'get book'


@api.route('', methods=['POST'])
def create_book():
    return 'create book'

