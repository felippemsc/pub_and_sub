# coding: utf-8
"""
Resource's View

Author: Felippe Costa <felippemsc@gmail.com>
"""
import json
import logging
import uuid

import redis

from falcon import HTTP_CREATED

from config import BaseConfig

from models.resource import Resource
from ..schemas import ResourceSchema
from ..services.publisher import PublisherConnection
from ..utils import use_args_with

LOG = logging.getLogger()
REDIS_SESSION = redis.Redis(host=BaseConfig.REDIS_HOST, port=BaseConfig.REDIS_PORT, db=0)


class ResourceCollection:
    """
    Collection of Messages
    """
    def __init__(self):
        self.pub_conn = PublisherConnection(exchange='teste_ex')
        pass

    @use_args_with(ResourceSchema)
    def on_post(self, request, response, args):
        """
        API to create new Messages
        """
        instance = Resource(args)
        instance.commit()

        args.update({"transaction_id": str(uuid.uuid4())})

        LOG.info(f"{json.dumps(args)}")
        status = REDIS_SESSION.set(args.get('transaction_id'), json.dumps(args))
        LOG.info(f"Resultado adicao ao Redis: {status}")

        self.pub_conn.publish('teste_key', args)

        response.status = HTTP_CREATED
        response.body = args

    # def on_get(self, request, response):
    #     """
    #     API to list the messages
    #     """
    #     url_params = request.params
    #
    #     categories = Category.get_list(url_params)
    #     if not categories:
    #         response.status = HTTP_NOT_FOUND
    #
    #     response.body = json.dumps({"categories": categories})


class CategoryResource:
    """
    Resource of a Message
    """
#     def on_get(self, request, response, id_):  # pylint: disable=W0613
#         """
#         API to retrieve one message by its id
#         """
#         url_params = request.params
#
#         category = Category.get_by_id(id_)
#         if not category:
#             response.status = HTTP_NOT_FOUND
#             return
#
#         response.body = json.dumps(
#             {"category": category.serialize(serialize_children=True,
#                                             children_params=url_params)})
#
#     def on_delete(self, request, response, id_):  # pylint: disable=W0613
#         """
#         API to delete one message by its id
#         """
#         category = Category.get_by_id(id_)
#         if not category:
#             response.status = HTTP_NOT_FOUND
#             return
#
#         category.delete()
#
#         msg = f"Record with id: {id_} was successfully deleted"
#         response.body = json.dumps({"msg": msg,
#                                     "category": category.serialize()})
#

    @use_args_with(ResourceSchema)
    def on_patch(self, request, response, args, id_):  # pylint: disable=W0613
        """
        API that updates one message by its id
        """
        response.status = HTTP_CREATED
        response.body = args
