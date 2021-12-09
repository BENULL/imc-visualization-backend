#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: BENULL
@time: 2021/12/8 下午8:56
"""
import os
from app import create_app
from werkzeug.exceptions import HTTPException
from app.exceptions.error import APIException
from app.exceptions.error_code import ServerError

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        status = 1007
        return APIException(msg, code, status)
    else:
        # 调试模式
        # log
        if not app.config['DEBUG']:
            return ServerError()
        else:
            raise e


if __name__ == '__main__':
    app.run()
