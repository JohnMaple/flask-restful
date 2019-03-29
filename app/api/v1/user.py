# -*- coding: utf-8 -*-
"""
    @description:
"""
from flask import jsonify, g

from app import db
from app.libs.error_code import DeleteSuccess
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.user import User

__author__ = 'Henry'


api = Redprint('user')


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def super_get_user(uid):
    """
    管理员查询用户
    :param uid:
    :return:
    """
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


@api.route('<int:uid>', methods=['DELETE'])
@auth.login_required
def super_delete_user():
    """
    管理员权限操作用户
    :return:
    """
    pass


@api.route('', methods=['GET'])
@auth.login_required
def get_user():
    """
    获取用户信息，可以使用view_model,严谨的restful没必要
    :param uid:
    :return:
    """
    uid = g.user.uid
    user = User.query.get_or_404(uid)
    return jsonify(user)


@api.route('', methods=['DELETE'])
@auth.login_required
def delete_user():
    """
    删除用户，防止超权
    :param uid:
    :return:
    """
    uid = g.user.uid    # flask实例是线程隔离的
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()

    return DeleteSuccess()





