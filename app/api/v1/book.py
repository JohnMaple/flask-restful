# -*- coding: utf-8 -*-
"""
    @description:
"""
from app.libs.redprint import Redprint

__author__ = 'Henry'

api = Redprint('book')


@api.route('/search', methods=['GET'])
def search():
    pass


@api.route('', methods=['GET'])
def get_book():
    return 'get book'


@api.route('', methods=['POST'])
def create_book():
    return 'create book'

