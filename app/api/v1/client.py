# -*- coding: utf-8 -*-
"""
    @description: 客户端（包括用户，第三方平台等）
"""
from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import ClientTypeError, Success
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm


__author__ = 'Henry'


api = Redprint('client')


@api.route('/register', methods=['POST'])
def create_client():
    # 参数校验 restfull 输入和输出必须是json格式的
    # 获取参数 request.json 和request.args.to_dict()
    # 1.优化验证，重新验证方法
    # 2.优化获取参数，在验证基类里面直接获取参数

    # data = request.json
    form = ClientForm().validate_for_api()

    # 注册客户端进行分业务实行
    promise = {
        ClientTypeEnum.USER_EMAIL: __register_user_by_email,
    }
    promise[form.type.data]()

    # 可以定以时的复杂，不能调用复杂
    return Success()

    # 没有对验证器进行重新的话需要这样
    # if form.validate():
    #     # 注册客户端进行分业务实行
    #     promise = {
    #         ClientTypeEnum.USER_EMAIL: __register_user_by_email,
    #     }
    #     promise[form.type.data]()
    # else:
    #     raise ClientTypeError()
    # return 'success'


def __register_user_by_email():
    # 没有nickname, 使用UserEmailForm来获取
    form = UserEmailForm().validate_for_api()

    User.register_by_email(form.nickname.data, form.account.data, form.secret.data)
    # if form.validate():
    #     User.register_by_email(form.nickname.data, form.account.data, form.secret.data)




