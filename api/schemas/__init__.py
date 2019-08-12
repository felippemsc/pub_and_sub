# coding: utf-8
"""Module views_schemas.py

Copyright (C) 2018 Órama DTVM.


"""
from marshmallow import Schema, fields


class ResourceSchema(Schema):
    """
    Schema para validação do POST e PUT de Resource
    """
    id = fields.Integer()
    name = fields.String(required=True)
