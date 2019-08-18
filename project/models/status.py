# coding: utf-8
"""
Status Model Module

Author: Felippe Costa <felippemsc@gmail.com>
"""
import json
import logging

from datetime import datetime

from ..backend import BACKEND_SESSION
from ..models import DATETIME_FORMAT
from ..schemas import StatusSchema

LOG = logging.getLogger(__name__)


class StatusBaseModel:
    """
    Base Status Model
    """
    _schema = StatusSchema

    def __init__(self, key, state=None, dh_last_stage=None):
        self._key = key
        self.state = state

        if dh_last_stage:
            self.dh_last_stage = dh_last_stage
        else:
            self.dh_last_stage = datetime.now().strftime(DATETIME_FORMAT)

    def set(self):
        serialized_status = self._schema().dumps(self)
        return BACKEND_SESSION.set(self._key, serialized_status.data)

    def get(self):
        value = BACKEND_SESSION.get(self._key)
        value = self._schema().loads(value)

        return StatusBaseModel(self._key, **value.data)
