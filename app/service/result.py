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
from app.service import model as modelService
from app.service import experiment as experimentService
from flask import current_app
import re
import datetime
import os
import json


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


def upload(file):
    ext = os.path.splitext(file.filename)[1]
    filepath = os.path.join(current_app.config.get('UPLOAD_PATH'),
                            (re.sub(r'[^0-9]', '', str(datetime.datetime.now())) + ext))
    file.save(filepath)
    with open(filepath) as file:
        data = json.load(file)

        model_data = data['model']
        model = Model.query.filter(Model.model_name == model_data["model_name"]).first()
        if model:
            model_data['model_id'] = model["model_id"]
            modelService.update(model_data)
        else:
            model_data['model_id'] = modelService.add(model_data)

        experiment_data = data['experiment']
        experiment = Experiment.query.filter(Experiment.experiment_name == experiment_data["experiment_name"]).first()
        experiment_data['model_id'] = model_data['model_id']
        if experiment:
            experiment_data['experiment_id'] = experiment["experiment_id"]
            experimentService.update(experiment_data)
        else:
            experimentService.add(experiment_data)

        samples = data['samples']
        resultImages = []
        resultDetails = []
        for sample in samples:
            resultImages.append(ResultImage.build(**sample, experiment_id=experiment_data["experiment_id"]))

        db.session.bulk_save_objects(resultImages, return_defaults=True)
        db.session.commit()

        for sample, resultImage in zip(samples, resultImages):
            for type in sample['type'].split(','):
                resultDetails.append(ResultDetail.build(resultImage.image_id, int(type)))
        db.session.bulk_save_objects(resultDetails)
        db.session.commit()

















