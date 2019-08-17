# coding: utf-8
"""
Exceptions Module

Author: Felippe Costa <felippemsc@gmail.com>
"""
import logging

import falcon

from sqlalchemy.exc import IntegrityError

from ..database import DBSESSION
from ..models import ModelExceptions, ObjectNotFound


class ExceptionHandler(Exception):
    """
    Exception handler
    """
    @classmethod
    def handle(cls, ex, req, resp, params):  # pylint: disable=W0613
        """
        Rollbacks the DB Session.

        In addition, handles the exceptions, logs it and raises the proper status code response.
        """
        DBSESSION.rollback()

        logger = logging.getLogger()
        log_msg = f"{req.method} for {req.relative_uri} {cls.get_payload(req)}"

        if isinstance(ex, falcon.HTTPError):
            logger.info(f"Treated error during: {log_msg}. Response status = {ex.status}")
            pass
        elif isinstance(ex, ModelExceptions):
            logger.info(f"Treated error during: {log_msg}. Response status = 400")
            ex = falcon.HTTPBadRequest(description=ex.args)
        elif isinstance(ex, ObjectNotFound):
            logger.info(f"Treated error during: {log_msg}. Response status = 404")
            ex = falcon.HTTPNotFound(description=ex.args)
        elif isinstance(ex, IntegrityError):
            logger.exception(f"Database integrity error during: {log_msg}. Response status = 500")
            ex = falcon.HTTPBadRequest()
        else:
            logger.exception(f"Unexpected error during: {log_msg}. Response status = 500")
            ex = falcon.HTTPInternalServerError()
        raise ex

    @staticmethod
    def get_payload(req):
        """Gets the payload string"""
        try:
            payload = req.media
            payload_msg = f"with payload: {payload}"
        except falcon.HTTPBadRequest:
            payload_msg = "without payload"

        return payload_msg
