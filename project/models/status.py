# coding: utf-8
"""
Status Model Module

Author: Felippe Costa <felippemsc@gmail.com>
"""
import logging

from datetime import datetime

from ..backend import BACKEND_SESSION
from ..constants import DATETIME_FORMAT, TIMEZONE
from ..schemas import StatusSchema

LOG = logging.getLogger(__name__)


class StatusBaseModel:
    """
    Base Status Model
    """
    _schema = StatusSchema

    # TODO: Abstrair mudança de status via model (colocar funções de mudanças de status no model)
    def __init__(self, key: str, state: str = None, last_log: str = None, logs: list = None, percentage: int = 0,
                 id_last_stage: int = 0, dh_last_stage: str = datetime.now(TIMEZONE).strftime(DATETIME_FORMAT)):
        """
        Instantiates Status Model
        """
        self._key = key
        self.state = state
        self.percentage = percentage
        self.last_log = last_log

        self.id_last_stage = id_last_stage
        self.dh_last_stage = dh_last_stage

        if logs is None:
            self.logs = []
        else:
            self.logs = logs

    def set(self):
        """
        Save the status on the redis result backend
        """
        serialized_status = self._schema().dumps(self)
        result = BACKEND_SESSION.set(self._key, serialized_status.data)
        if not result:
            LOG.warning(f"Error during the set of {serialized_status.data} for key = {self._key}")
            return

        return serialized_status.data

    @classmethod
    def get(cls, key):
        """
        Gets the status on the redis result backend
        """
        value = BACKEND_SESSION.get(key)
        if not value:
            return

        value = cls._schema().loads(value)
        return StatusBaseModel(key, **value.data)

    # def init_new_stage(self):
    #     self.id_last_stage += 1
    #     self.dh_last_stage = datetime.now(TIMEZONE).strftime(DATETIME_FORMAT)
    #     self.logs.append(LogsBaseModel(self.id_last_stage))
    #
    # def log(self, msg: str, id_stage: int = None):
    #     if id_stage is None:
    #         id_stage = self.id_last_stage
    #
    #     log_group = self.get_log_group_by_stage(id_stage)
    #     log_group.append(msg)
    #
    # def get_log_group_by_stage(self, id_stage: int):
    #     for log_group in self.logs:
    #         if id_stage == log_group.id_stage:
    #             return log_group


class LogObject:
    """
    Log Object
    """
    def __init__(self, id_stage: int, logs_stage: list = None):
        """
        Instantiates Log Object
        """
        self.id_stage = id_stage

        if logs_stage is None:
            self.logs_stage = []
        else:
            self.logs_stage = logs_stage

    # def append(self, new_log_msg: str):
    #     self.logs_stage.append(new_log_msg)
