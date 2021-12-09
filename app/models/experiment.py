#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: BENULL
@time: 2021/12/9 上午11:36
"""
from app.models.base import Base
from sqlalchemy import Column, DateTime, Float, String, text, orm
from sqlalchemy.dialects.mysql import INTEGER


class Experiment(Base):
    __tablename__ = 'experiment'

    experiment_id = Column(INTEGER(11), primary_key=True, comment='实验 id')
    model_id = Column(INTEGER(11), nullable=False, comment='模型 id')
    threshold = Column(Float, comment='实验阈值')
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
                         comment='最近一次修改时间')
    experiment_name = Column(String(100), comment='实验名称')
    f1_score = Column(Float)
    precision = Column(Float)
    recall = Column(Float)
    epoch = Column(INTEGER(11))
    lr = Column(Float)
    batchsize = Column(INTEGER(11))
    test_time = Column(DateTime)
    end_time = Column(DateTime)

    @orm.reconstructor
    def __init__(self):
        self.fields = ['experiment_id', 'model_id', 'threshold', 'experiment_name',
                       'f1_score',
                       'precision', 'recall', 'epoch', 'lr',
                       'batchsize',
                       'test_time', 'end_time']


    @staticmethod
    def build(model_id, threshold, experiment_name, f1_score, precision, recall, epoch, lr, batchsize,
                 test_time, **kwargs):
        experiment = Experiment()
        experiment.model_id = model_id
        experiment.threshold = threshold
        experiment.experiment_name = experiment_name
        experiment.f1_score = f1_score
        experiment.precision = precision
        experiment.recall = recall
        experiment.epoch = epoch
        experiment.lr = lr
        experiment.batchsize = batchsize
        experiment.test_time = test_time
        return experiment
