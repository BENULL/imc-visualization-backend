#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: BENULL
@time: 2021/12/9 上午11:39
"""
from app.models.base import Base
from sqlalchemy import Column, DateTime, LargeBinary, String, text, orm, Text
from sqlalchemy.dialects.mysql import INTEGER


class Model(Base):
    __tablename__ = 'model'

    model_id = Column(INTEGER(11), primary_key=True, comment='模型 id')
    model_name = Column(String(100), nullable=False, unique=True, comment='模型名')
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
                         comment='最近一次修改时间')
    description = Column(String(500))
    params = Column(INTEGER(11))
    structure = Column(Text)

    @orm.reconstructor
    def __init__(self,):
        self.fields = ['model_id', 'model_name', 'description', 'params',
                       'structure']
    @staticmethod
    def build(model_name, description, params, structure, **kwargs):
        model = Model()
        model.model_name = model_name
        model.description = description
        model.params = params
        model.structure = structure
        return model


