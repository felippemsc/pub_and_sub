# coding: utf-8
"""Module category

ORM of Base Project: resource model.

Author: Felippe Costa <felippemsc@gmail.com>
"""
from sqlalchemy import Integer, Text
from sqlalchemy.schema import Column

from api.schemas import ResourceSchema

from models import BaseModel

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
DATE_FORMAT = "%Y-%m-%d"


class Resource(BaseModel):
    """
    Category's Model
    """
    __tablename__ = 'resource'
    serializer = ResourceSchema

    id = Column("id_category", Integer, primary_key=True, autoincrement=True)
    name = Column("nm_category", Text, nullable=False, unique=True)
