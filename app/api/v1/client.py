# -*- coding: utf-8 -*-
"""
    @description: 客户端（包括用户，第三方平台等）
    @copyright: (c) 2019/3/27 16:08 by Henry.
"""
from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm

__author__ = 'Henry'


api = Redprint('client')


@api.route('/register', methods=['POST'])
def create_client():
    # 参数校验 restfull 输入和输出必须是json格式的
    # 获取参数 request.json 和request.args.to_dict()
    data = request.json
    form = ClientForm(data=data)

    if form.validate():
        # 注册客户端进行分业务实行
        promise = {
            ClientTypeEnum.USER_EMAIL: __register_user_by_email,
        }
        promise[form.type.data]()

    return 'success'


def __register_user_by_email():
    # 没有nickname, 使用UserEmailForm来获取
    form = UserEmailForm(data=request.json)
    if form.validate():
        User.register_by_email(form.nickname.data, form.account.data, form.secret.data)




