# -*- coding: utf-8 -*-
"""
    @description: api 授权
    @copyright: (c) 2019/3/28 14:05 by Henry.
"""
from flask import current_app, jsonify
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import AuthFailed
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm, TokenForm

__author__ = 'Henry'


api = Redprint('token')


@api.route('', methods=['POST'])
def get_token():
    form = ClientForm().validate_for_api()

    promise = {
        ClientTypeEnum.USER_EMAIL: User.verify,
    }

    # 身份验证
    identity = promise[ClientTypeEnum(form.type.data)](form.account.data, form.secret.data)

    expiration = current_app.config['TOKEN_EXPIRATION']

    # 生成token
    token = generate_auth_token(identity['uid'], form.type.data, identity['scope'], expiration)

    data = dict(
        token=token.decode('utf-8')
    )

    return jsonify(data), 201


@api.route('/secret', methods=['POST'])
def get_token_info():
    """
    验证令牌有效期或获取令牌的明文信息
    :return:
    """
    form = TokenForm().validate_for_api()
    serializer = Serializer(current_app.config['SECRET_KEY'])

    data1 = serializer.loads(form.token.data)

    try:
        data = serializer.loads(form.token.data, return_header=True)
    except BadSignature:
        raise AuthFailed(msg='token is invalid', error_code=1002)
    except SignatureExpired:
        raise AuthFailed(msg='token is expired', error_code=1003)

    result = dict(
        uid=data[0]['uid'],
        scope=data[0]['scope'],
        create_at=data[1]['iat'],
        expire_in=data[1]['exp'],
    )

    return jsonify(result)


def generate_auth_token(uid, ac_type, scope=None, expiration=7200):
    """
    生成令牌
    :param uid: 用户id
    :param ac_type: 客户端类型
    :param scope: 权限
    :param expiration: 有效期
    :return: token
    """
    serializer = Serializer(current_app.config['SECRET_KEY'], expiration)

    return serializer.dumps({'uid': uid, 'type': ac_type.value, 'scope': scope})




