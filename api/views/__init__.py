# coding: utf-8
"""
Base Views Module

Author: Felippe Costa <felippemsc@gmail.com>
"""
import os


class RootResource:
    """
    ...
    """
    def on_get(self, request, response):  # pylint: disable=W0613
        """
        Method get for test resource
        """
        response.body = (f'Falcon Project - Publisher and Subscriber\n'
                         f'Version:{os.getenv("API_VERSION")}')
