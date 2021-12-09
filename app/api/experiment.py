#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: BENULL
@time: 2021/12/9 下午2:20
"""
from flask import request

from app.api import api, ServerResponse
from app.exceptions.error import APIException
from app.service.experiment import fetch, add, update, fetchModelAndExp


@api.route('/experiment/fetchAll', methods=['POST'])
def searchExperiment():
    try:
        params = request.get_json()
        data = fetch(params)
        return ServerResponse.createBySuccess(data=data)
    except APIException:
        return ServerResponse.createByError(msg="获取失败")


@api.route('/experiment/add', methods=['POST'])
def addExperiment():
    try:
        experiment = request.get_json()
        add(experiment)
        return ServerResponse.createBySuccess(msg='添加成功')
    except APIException:
        return ServerResponse.createByError(msg="添加失败")


@api.route('/experiment/update', methods=['POST'])
def updateExperiment():
    try:
        experiment = request.get_json()
        update(experiment)
        return ServerResponse.createBySuccess(msg='更新成功')
    except APIException:
        return ServerResponse.createByError(msg="更新失败")


@api.route('/experiment/getCategory')
def getCategory():
    try:
        category = fetchModelAndExp()
        return ServerResponse.createBySuccess(data=category)
    except APIException:
        return ServerResponse.createByError(msg="获取失败")

