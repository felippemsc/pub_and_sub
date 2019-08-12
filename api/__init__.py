# coding: utf-8
"""
App creation

Author: Felippe Costa <felippemsc@gmail.com>
"""
import falcon

from database import init_db

from .views import RootResource
from .views.resource import ResourceCollection


def create_app(app_settings):
    """
    Application factory

    :param app_settings: a configuration object
    :return: An application Falcon object
    """
    # Application inicialization
    app = falcon.API(middleware=[])
    # app.add_error_handler(Exception, ExceptionHandler.handle)

    init_db(app_settings.DATABASE_URI)

    # APIs
    app.add_route('/', RootResource())
    app.add_route('/resource', ResourceCollection())

    return app
