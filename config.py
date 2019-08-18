import logging.config
import os

LOG = logging.getLogger()


class BaseConfig:
    API_VERSION = os.getenv('API_VERSION')

    LOG.info(f'Config Publisher and Subscriber Base Project. Version:{API_VERSION}')

    RABBIT_USER = os.getenv('RABBIT_USER', 'rabbit')
    RABBIT_PASS = os.getenv('RABBIT_PASS', 'password')
    RABBIT_HOST = os.getenv('RABBIT_HOST', '172.31.0.4')

    REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
    REDIS_PORT = os.getenv('REDIS_PORT', 6379)

    DB_NAME = os.getenv('DB_ENDPOINT', 'base_db')
    DB_SCHEMA = os.getenv('DB_SCHEMA', 'base_schema')
    DB_HOST = os.getenv('DB_HOST', '127.0.0.1')
    DB_PORT = os.getenv('DB_PORT', 3306)
    DB_USER = os.getenv('DB_USER', 'root')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
    DATABASE_URI = os.getenv('DATABASE_URI', f'mysql+mysqldb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')


class TestConfig(BaseConfig):
    TESTING = True

    RABBIT_USER = os.getenv('RABBIT_USER')
    RABBIT_PASS = os.getenv('RABBIT_PASS')
    RABBIT_HOST = os.getenv('RABBIT_HOST')

    REDIS_HOST = os.getenv('REDIS_HOST')
    REDIS_PORT = os.getenv('REDIS_PORT')

    DB_NAME = os.getenv('DB_ENDPOINT')
    DB_SCHEMA = os.getenv('DB_SCHEMA')
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DATABASE_URI = os.getenv('DATABASE_URI')
