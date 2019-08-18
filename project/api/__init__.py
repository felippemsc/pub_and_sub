# coding: utf-8
"""
Publisher and Subscriber Service

Author: Felippe Costa <felippemsc@gmail.com>
"""
import falcon

from ..backend import init_backend
from ..database import init_db

from .exception_handler import ExceptionHandler
from .middleware import DatabaseSessionManager
from .views import RootResource
from .views.example import ExampleCollection, ExampleResource


def create_app(app_settings):
    """
    Application factory

    :param app_settings: a configuration object
    :return: An application Falcon object
    """
    app = falcon.API(middleware=[DatabaseSessionManager()])
    app.add_error_handler(Exception, ExceptionHandler.handle)

    init_db(app_settings.DATABASE_URI)
    init_backend(app_settings.REDIS_HOST, app_settings.REDIS_PORT)

    # APIs
    app.add_route('/', RootResource())
    app.add_route('/test', ExampleCollection())
    app.add_route('/test/{id_:int}', ExampleResource())

    return app
