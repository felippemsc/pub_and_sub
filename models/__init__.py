# coding: utf-8
"""
Base Models

Author: Felippe Costa <felippemsc@gmail.com>
"""
from sqlalchemy.ext.declarative import AbstractConcreteBase
from sqlalchemy.exc import IntegrityError

from database import BASE, DBSESSION

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
DATE_FORMAT = "%Y-%m-%d"


class BaseModel(AbstractConcreteBase, BASE):
    """
    Base Model
    """
    __tablename__ = None
    serializer = None

    def __init__(self, data: dict):
        for key in data:
            model_att = getattr(self.__class__, key, None)
            value = data.get(key)

            setattr(self, key, type(model_att.type.python_type())(value))

    def update(self, data: dict):
        """
        Validates and updates a new registry
        :param data: dictionary with data
        :return: instantiated object
        """
        for key in data:
            model_att = getattr(self.__class__, key, None)
            value = data.get(key)

            setattr(self, key, type(model_att.type.python_type())(value))

        self.commit()

    def commit(self):
        """
        Commit a record to the database
        """
        try:
            DBSESSION.add(self)
            DBSESSION.commit()
        except IntegrityError:
            DBSESSION.rollback()
            raise

    def delete(self):
        """
        Deletes a record from the database
        """
        DBSESSION.delete(self)
        DBSESSION.commit()
