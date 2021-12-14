#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: BENULL
@time: 2021/12/9 下午2:39
"""
from app.models.model import Model
from app.models.base import db


def fetch(params):
    if not params:
        data = Model.query.all()
    else:
        pagination = Model.query.filter(Model.model_name.like(f'%{params["input"]}%')) \
            .paginate(params['page'],
                      params['pageSize'],
                      error_out=False)
        data = dict(items=pagination.items,
                    pager=dict(index=pagination.page,
                               total=pagination.total,
                               size=pagination.per_page))
    return data


def add(model):
    with db.auto_commit():
        model = Model.build(**model)
        db.session.add(model)
    return model.model_id


def update(model):
    with db.auto_commit():
        Model.query.filter(Model.model_id == model['model_id']).update(model)
    return True



