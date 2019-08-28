# coding: utf-8
"""
Modulo View Example

Author: Felippe Costa <felippemsc@gmail.com>
"""
import json
import logging

from falcon import HTTP_CREATED, HTTP_NO_CONTENT
from webargs.falconparser import use_args

from ...models.example import Example
from ...schemas import ExampleSchema, QueryStringSchema

LOG = logging.getLogger()


class ExampleCollection:
    """
    Example Collection
    """
    model = Example

    @use_args(ExampleSchema)
    def on_post(self, request, response, payload):
        """
        Creates an Example resource
        """
        instance = self.model(**payload).commit()

        response.status = HTTP_CREATED
        response.body = json.dumps(instance.to_dict(excluding=['status']))

    @use_args(QueryStringSchema, locations=('query',))
    def on_get(self, request, response, query_sring):
        """
        Lists Example Resources
        """
        limit = query_sring.get('limit')
        offset = query_sring.get('offset')

        instance_list = self.model.get_many(limit, offset)

        response.body = json.dumps({"limit": limit,
                                    "offset": offset,
                                    "examples": self.model.serialize_many(instance_list, excluding=["status.logs"])})


class ExampleResource:
    """
    Example Resource
    """
    model = Example

    def on_get(self, request, response, id_):
        """
        Gets an Example resource
        """
        instance = self.model.get(id_)

        response.body = json.dumps(instance.to_dict())

    def on_delete(self, request, response, id_):
        """
        Deletes an Example resource
        """
        instance = self.model.get(id_)
        instance.delete()

        response.status = HTTP_NO_CONTENT

    @use_args(ExampleSchema(partial=True))
    def on_patch(self, request, response, payload, id_):
        """
        Updates an Example resource
        """
        instance = self.model.get(id_)
        instance = instance.update(payload)

        response.body = json.dumps({instance.to_dict()})

    @use_args(ExampleSchema)
    def on_put(self, request, response, payload, id_):
        """
        Updates an Example resource
        """
        instance = self.model.get(id_)
        instance = instance.update(payload)

        response.body = json.dumps({instance.to_dict()})

