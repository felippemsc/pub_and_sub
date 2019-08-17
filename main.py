import click

from config import BaseConfig

from project.api import create_app
# from project.consumer import create_consumer


@click.group()
def cli():
    pass


# # @cli.option('--queue', help='Queue to consume.')
# @cli.command()
# @click.option('-w', default=1, help='Number of workers.')
# def init_consumer(w):
#     workers = w
#     create_consumer(BaseConfig, workers, queue='teste')


if __name__ == '__main__':
    cli()

app = create_app(BaseConfig)