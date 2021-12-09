#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: BENULL
@time: 2021/12/9 下午2:20
"""
from flask import request

from app.api import api, ServerResponse
from app.exceptions.error import APIException
from app.service.model import fetch, add, update


@api.route('/model/fetchAll', methods=['POST'])
def searchModel():
    try:
        params = request.get_json()
        data = fetch(params)
        return ServerResponse.createBySuccess(data=data)
    except APIException:
        return ServerResponse.createByError(msg="获取失败")


@api.route('/model/add', methods=['POST'])
def addModel():
    try:
        model = request.get_json()
        add(model)
        return ServerResponse.createBySuccess(msg='添加成功')
    except APIException:
        return ServerResponse.createByError(msg="添加失败")


@api.route('/model/update', methods=['POST'])
def updateModel():
    try:
        model = request.get_json()
        update(model)
        return ServerResponse.createBySuccess(msg='更新成功')
    except APIException:
        return ServerResponse.createByError(msg="更新失败")

