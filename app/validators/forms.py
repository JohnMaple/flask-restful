# -*- coding: utf-8 -*-
"""
    @description:
    @copyright: (c) 2019/3/27 16:15 by Henry.
"""
from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired

__author__ = 'Henry'


class ClientForm(Form):
    account = StringField(validators=[DataRequired()])
    secret = StringField()
    type = IntegerField()
    pass



