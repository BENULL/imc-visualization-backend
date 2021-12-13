#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: BENULL
@time: 2021/12/8 下午8:57
"""
from flask import Blueprint, jsonify

api = Blueprint('api', __name__)
class ServerResponse:
    @staticmethod
    def createBySuccess(status=0, data=None, msg=None):
        response = dict(status=status)
        if data:
            response['data'] = data
        if msg:
            response['msg'] = msg
        return jsonify(response)

    @staticmethod
    def createByError(status=1, msg=None):
        response = dict(status=status)
        if msg:
            response['msg'] = msg
        return jsonify(response)


from app.api import model, experiment, result




