# -*- coding: utf-8 -*-
"""
    @description: 
    @copyright: (c) 2019/3/21 16:47 by Henry.
"""
from flask import Blueprint
from app.api.v1 import user, book

__author__ = 'Henry'


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)

    user.api.register(bp_v1)
    book.api.register(bp_v1)

    return bp_v1




