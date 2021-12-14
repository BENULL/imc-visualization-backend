#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: BENULL
@time: 2021/12/9 下午8:22
"""
from flask import request

from app.api import api, ServerResponse
from app.exceptions.error import APIException
from app.service.result import fetch, upload


@api.route('/result/fetchResult', methods=['POST'])
def searchResult():
    try:
        params = request.get_json()
        data = fetch(params)
        return ServerResponse.createBySuccess(data=data)
    except APIException:
        return ServerResponse.createByError(msg="获取失败")


@api.route('/result/upload', methods=['POST'])
def uploadResult():
    try:
        file = request.files.get("file")
        upload(file)
        return ServerResponse.createBySuccess(msg="上传成功")
    except APIException:
        return ServerResponse.createByError(msg="上传失败")
