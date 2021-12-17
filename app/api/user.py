#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: BENULL
@time: 2021/12/9 下午2:20
"""
from flask import request, current_app

from app.api import api, ServerResponse


@api.route('/users/login', methods=['POST'])
def login():
    params = request.get_json()
    if params['username'] == "admin" and params['password'] == "123456":
        return ServerResponse.createBySuccess(data={'accessToken': current_app.config['SECRET_KEY']})
    else:
        return ServerResponse.createByError(status=403, msg="登录失败")
