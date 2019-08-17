# coding: utf-8
"""
Base View Module

Author: Felippe Costa <felippemsc@gmail.com>
"""
import os


class RootResource:
    """
    ...
    """
    def on_get(self, request, response):  # pylint: disable=W0613
        """
        Health check route
        """
        response.body = (f'Publisher and Subscriber Base Project\n'
                         f'Version:{os.getenv("API_VERSION")}')
