#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: BENULL
@time: 2021/12/9 上午11:43
"""
from app.models.base import Base
from sqlalchemy import Column, DateTime, String, text, orm
from sqlalchemy.dialects.mysql import INTEGER


class ResultDetail(Base):
    __tablename__ = 'result_detail'

    detail_id = Column(INTEGER(11), primary_key=True, comment='结果类型 id')
    image_id = Column(INTEGER(11), nullable=False, comment='图像结果 id')
    type = Column(INTEGER(11), comment='类型')
    bounding_box = Column(String(200), comment='边界框')
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"), comment='最近一次修改时间')

    @orm.reconstructor
    def __init__(self):
        self.fields = ['detail_id', 'image_id', 'type', 'bounding_box']