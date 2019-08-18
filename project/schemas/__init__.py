# coding: utf-8
"""
Schemas Module

Author: Felippe Costa <felippemsc@gmail.com>
"""
from marshmallow import Schema, fields, post_load, validate


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

    class Meta:
        strict = True


class StatusSchema(Schema):
    """
    Schema for Status validation and serialization
    """
    state = fields.String(allow_none=True, validate=validate.Length(max=1))
    dh_last_stage = fields.String()

    class Meta:
        strict = True


# numbers = fields.List(fields.Float())
#
# {
#     "status":
#         {
#             "situacao": "P",
# 	    "porcentagem": 75,
#       "dh_ultima_etapa": "",
# 	    "id_ultima_etapa": 1,
# 	    "ultimo_log": "Aguardando processamento em fila",
# 	    "logs": [
#                 {
#                     "id_etapa": 1,
#                     "logs_etapa": [
#                         "log teste um",
#                         "log teste dois"
#                     ]
#                 },
#                 {
#                     "id_etapa": 2,
# 		    "logs_etapa": [
#                         "log teste um",
#                         "log teste dois"
#                     ]
#                 }
#             ],
#         }
# }
