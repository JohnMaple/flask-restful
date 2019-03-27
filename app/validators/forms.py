# -*- coding: utf-8 -*-
"""
    @description:
    @copyright: (c) 2019/3/27 16:15 by Henry.
"""
from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, length, Email, Regexp, ValidationError

from app.libs.enums import ClientTypeEnum
from app.models.user import User

__author__ = 'Henry'


class ClientForm(Form):
    account = StringField(validators=[DataRequired(), length(min=5, max=32)])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self, value):
        try:
            client = ClientTypeEnum(value.data)  # 通过值获取枚举名称 client 是枚举类型
        except ValueError as e:
            raise e
        self.type.data = client


class UserEmailForm(ClientForm):
    account = StringField(validators=[Email(message='invalidate email')])
    secret = StringField(validators=[DataRequired(), Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}&')])
    nickname = StringField(validators=[DataRequired(), length(min=2, max=22)])

    def validate_account(self, value):
        """
        账号是否唯一
        :return:
        """
        if User.query.filter_by(email=value.data).first():
            raise ValidationError()








