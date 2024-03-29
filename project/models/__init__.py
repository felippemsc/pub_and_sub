# coding: utf-8
"""
Base Model Module

Author: Felippe Costa <felippemsc@gmail.com>
"""
import logging

from sqlalchemy.ext.declarative import AbstractConcreteBase
from sqlalchemy.exc import IntegrityError

from ..database import BASE, DBSESSION

LOG = logging.getLogger(__name__)

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
DATE_FORMAT = "%Y-%m-%d"


class ModelExceptions(Exception):
    """Models Exceptions"""


class ObjectNotFound(Exception):
    """Instance Not Found Excepetion"""


class BaseModel(AbstractConcreteBase, BASE):
    """
    Base Model
    """
    __tablename__ = None
    _serializer = None
    str_representation = None

    def __init__(self, *args, **kwargs):
        """
        Instantiates the object
        """
        super(BaseModel, self).__init__(*args, **kwargs)

    def to_dict(self):
        """
        Serialize the object to a dict

        :return: dict representation of the object
        """
        serialized = self._serializer().dump(self)
        return serialized.data

    @classmethod
    def serialize_many(cls, instances: list):
        """
        Serialize the object to a dict

        :return: list of dicts representing the objects
        """
        serialized = cls._serializer(many=True).dump(instances)
        return serialized.data

    @classmethod
    def get(cls, id_: int):
        """
        Gets an objects instance for a given ID.

        :param id_: records ID
        :return: instance
        """
        query = DBSESSION.query(cls)
        instance = query.get(id_)
        if not instance:
            raise ObjectNotFound(f"Register of {cls.str_representation} not found for id = {id_}.")
        return instance

    @classmethod
    def get_many(cls, limit: int = 100, offset: int = 0):
        """
        List the resources using the limit and offset to paginate it

        :param limit: integer
        :param offset: integer
        :return: list of objects
        """
        if limit > 100:
            raise ModelExceptions("It is not possible to list more than 100 resources.")

        instance_list = DBSESSION.query(cls)
        instance_list = instance_list.order_by(cls.id)
        instance_list = instance_list.offset(offset)
        instance_list = instance_list.limit(limit)
        instance_list = instance_list.all()
        if not instance_list:
            raise ObjectNotFound(f"No registers of {cls.str_representation} found")

        return instance_list

    @classmethod
    def count(cls):
        """
        Counts the number of row of the table related to the object

        :return: integer
        """
        return DBSESSION.query(cls).count()

    def update(self, data: dict):
        """
        Updates a given registry

        :param data: dictionary with data to update
        :return: commited object
        """
        for key in data:
            model_att = getattr(self.__class__, key, None)
            value = data.get(key)

            setattr(self, key, type(model_att.type.python_type())(value))

        self.commit()
        return self

    def commit(self):
        """
        Commit a record to the database
        """
        try:
            DBSESSION.add(self)
            DBSESSION.commit()
            return self
        except IntegrityError:
            DBSESSION.rollback()
            raise

    def delete(self):
        """
        Deletes a record from the database
        """
        DBSESSION.delete(self)
        DBSESSION.commit()
        LOG.info(f"Register of {self.str_representation} with id = {self.id} was successfully deleted.")
