# coding: utf-8
"""
Schemas Module

Author: Felippe Costa <felippemsc@gmail.com>
"""
from marshmallow import Schema, fields, post_load, validate

from ..constants import TP_STATUS


class QueryStringSchema(Schema):
    """
    Schema for pagination query string validation and serialization
    """
    limit = fields.Integer()
    offset = fields.Integer()

    @post_load
    def set_default(self, out_data):
        """
        Limits limit pagination to 100 and set the defaults of offset to 0
        """
        limit = out_data.get('limit')
        offset = out_data.get('offset')

        if limit is None or limit > 100:
            out_data["limit"] = 100

        if offset is None:
            out_data["offset"] = 0

        return out_data

    class Meta:
        strict = True


class ExampleSchema(Schema):
    """
    Schema for Example validation and serialization
    """
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(max=50))
    status = fields.Nested("StatusSchema", dump_only=True)

    class Meta:
        strict = True


class StatusSchema(Schema):
    """
    Schema for Status serialization
    """
    state = fields.String(allow_none=True, validate=validate.OneOf(TP_STATUS))
    percentage = fields.Integer(allow_none=True)
    last_log = fields.String(allow_none=True)
    id_last_stage = fields.Integer(allow_none=True)
    dh_last_stage = fields.String()
    logs = fields.Nested("LogsSchema", many=True)

    class Meta:
        strict = True


class LogsSchema(Schema):
    """
    Schema for Logs serialization
    """
    id_etapa = fields.Integer(allow_none=True)
    logs_etapa = fields.List(fields.String(allow_none=True))

    class Meta:
        strict = True
