#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: BENULL
@time: 2021/12/9 上午11:41
"""
from app.models.base import Base
from sqlalchemy import Column, DateTime, Float, String, text, orm
from sqlalchemy.dialects.mysql import INTEGER


class ResultImage(Base):
    __tablename__ = 'result_image'

    image_id = Column(INTEGER(11), primary_key=True, comment='图像结果 id')
    image_src = Column(String(100), nullable=False, comment='图像 src')
    experiment_id = Column(INTEGER(11), nullable=False, comment='实验 id')
    score = Column(Float, nullable=False, comment='得分')
    mask_src = Column(String(100), nullable=False, comment='掩码 src')
    label_src = Column(String(100), nullable=False, comment='标签 src')
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
                         comment='最近一次修改时间')

    @orm.reconstructor
    def __init__(self):
        self.fields = ['image_id', 'image_src', 'experiment_id', 'score', 'mask_src', 'label_src']
