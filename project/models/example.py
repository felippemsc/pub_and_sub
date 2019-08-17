# coding: utf-8
"""
Example Model Module

Author: Felippe Costa <felippemsc@gmail.com>
"""
from sqlalchemy import Integer, String
from sqlalchemy.schema import Column

from project.models import BaseModel
from project.schemas import ExampleSchema

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
DATE_FORMAT = "%Y-%m-%d"


class Example(BaseModel):
    """
    Category's Model
    """
    __tablename__ = 'example'
    _serializer = ExampleSchema
    str_representation = 'Example'

    id = Column("id_example", Integer, primary_key=True, autoincrement=True)
    name = Column("nm_example", String(50), nullable=False, unique=True)
