#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: BENULL
@time: 2021/12/9 下午2:39
"""
from app.models.experiment import Experiment
from app.models.base import db


def fetch(params):
    if not params:
        data = Experiment.query.all()
    else:
        pagination = Experiment.query.filter(Experiment.experiment_name.like(f'%{params["input"]}%')) \
            .paginate(params['page'],
                      params['pageSize'],
                      error_out=False)
        data = dict(items=pagination.items,
                    pager=dict(index=pagination.page,
                               total=pagination.total,
                               size=pagination.per_page))
    return data


def add(experiment):
    with db.auto_commit():
        experiment = Experiment.build(**experiment)
        db.session.add(experiment)
    return True


def update(experiment):
    with db.auto_commit():
        Experiment.query.filter(Experiment.experiment_id == experiment['experiment_id']).update(experiment)
    return True



