import logging.config
import os

LOG = logging.getLogger()


class BaseConfig:
    API_VERSION = os.getenv('API_VERSION')

    LOG.info(f'Config Falcon Base Project. Version:{API_VERSION}')

    RABBIT_USER = os.getenv('RABBIT_USER', 'rabbit')
    RABBIT_PASS = os.getenv('RABBIT_PASS', 'password')
    RABBIT_HOST = os.getenv('RABBIT_HOST', '172.26.0.2')

    REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
    REDIS_PORT = os.getenv('REDIS_PORT', 6379)

    DB_NAME = os.getenv('DB_ENDPOINT', 'base_db')
    DB_SCHEMA = os.getenv('DB_SCHEMA', 'base_schema')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', 3306)
    DB_USER = os.getenv('DB_USER', 'example')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
    DATABASE_URI = os.getenv('DATABASE_URI', f'mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
