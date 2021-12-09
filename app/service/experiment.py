#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: BENULL
@time: 2021/12/9 下午2:39
"""
from app.models.experiment import Experiment
from app.models.model import Model
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


def fetchModelAndExp():
    data = []
    models = Model.query.all()
    for m in models:
        modelExpInfo = dict(label=m.model_name, value=m.model_id)
        exps = [
            dict(label=exp.experiment_name, value=exp.experiment_id, test_time=exp.test_time, threshold=exp.threshold)
            for exp in Experiment.query.filter(Experiment.model_id == m.model_id).all()]
        modelExpInfo['children'] = exps
        data.append(modelExpInfo)
    return data
