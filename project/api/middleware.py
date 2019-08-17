# coding: utf-8
"""
Middleware Module

Author: Felippe Costa <felippemsc@gmail.com>
"""
import logging

from ..database import DBSESSION

LOG = logging.getLogger(__name__)


class DatabaseSessionManager:
    """
    Removes the SQLAlchemy's session after each request
    """
    def process_response(self, req, resp, resource, req_succeeded):
        """
        Process the response for the given request and removes the active DB Session
        """
        DBSESSION.remove()
