# coding: utf-8
"""
Module backend

Author: Felippe Costa <felippemsc@gmail.com>
"""
import redis


class RedisSession:
    def __init__(self):
        self.__conn = None

    def create_connection(self, host, port):
        self.__conn = redis.Redis(host=host, port=port, db=0)

    def set(self, key, value):
        return self.__conn.set(key, value)

    def get(self, key):
        return self.__conn.get(key)

    def delete(self, key):
        return self.__conn.delete(key)


BACKEND_SESSION = RedisSession()


def init_backend(host, port):
    """
    Configures the access to the backend result.
    """
    BACKEND_SESSION.create_connection(host, port)
