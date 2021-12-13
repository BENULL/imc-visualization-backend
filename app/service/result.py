#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: BENULL
@time: 2021/12/9 下午2:39
"""
from app.models.experiment import Experiment
from app.models.model import Model
from app.models.result_detail import ResultDetail
from app.models.result_image import ResultImage
from app.models.base import db


def fetch(params):
    model_name = Model.query.filter(Model.model_id==params['model_id']).first().model_name
    experiment = Experiment.query.filter(Experiment.experiment_id==params['experiment_id']).first()
    data = dict(model_name=model_name,
                experiment_name=experiment.experiment_name,
                results=[])
    threshold = experiment.threshold
    res = db.session.query(ResultDetail.bounding_box,ResultDetail.type, ResultImage.score,ResultImage.image_src,ResultImage.label_src,ResultImage.mask_src).join(ResultDetail, ResultImage.image_id == ResultDetail.image_id, isouter=True)\
        .filter(ResultImage.experiment_id == experiment.experiment_id)\
        .filter(ResultImage.image_src.like(f'%{params["search"]}%')) \
        .filter(params['left'] <= ResultImage.score)\
        .filter(ResultImage.score <= params['right'])
    if not params['pos']:
        res.filter(ResultImage.score < threshold)
    if not params['neg']:
        res.filter(ResultImage.score > threshold)
    data['results'] = res.all()

    return data
