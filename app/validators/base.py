# -*- coding: utf-8 -*-
"""
    @description:
"""
from flask import request
from wtforms import Form

from app.libs.error_code import ParameterException

__author__ = 'Henry'


class BaseForm(Form):
    def __init__(self):
        # 获取body参数
        data = request.get_json(silent=True)
        # 获取查询参数
        args = request.args.to_dict()
        super(BaseForm, self).__init__(data=data, **args)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()

        if not valid:
            # 所有错误信息存在 form.errors
            raise ParameterException(msg=self.errors)

        return self


