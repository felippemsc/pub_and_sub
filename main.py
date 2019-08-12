import click
import logging

from config import BaseConfig

from api import create_app
from consumer import create_consumer


@click.group()
def cli():
    pass


# @cli.option('--queue', help='Queue to consume.')
@cli.command()
@click.option('-w', default=1, help='Number of workers.')
def init_consumer(w):
    workers = w
    create_consumer(BaseConfig, workers, 'teste')


# @cli.command()
# def createdb():
#     logging.info('Creating the database to run the app locally')
#     init_db_local(BaseConfig.DATABASE_URI)


if __name__ == '__main__':
    cli()


app = create_app(BaseConfig)
