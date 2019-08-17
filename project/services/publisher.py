# import json
# import logging
#
# import pika
#
# from retry import retry
#
# from config import BaseConfig as cfg
#
# LOG = logging.getLogger(__name__)
#
#
# class PublisherConnection:
#     def __init__(self, exchange):
#         self.exchange = exchange
#
#         credentials = pika.PlainCredentials(cfg.RABBIT_USER, cfg.RABBIT_PASS)
#
#         self.connection = pika.BlockingConnection(
#             pika.ConnectionParameters(host=cfg.RABBIT_HOST, credentials=credentials))
#         self.channel = self.connection.channel()
#
#         self.channel.confirm_delivery()
#         self.channel.exchange_declare(exchange=exchange, exchange_type='direct')
#
#     @retry(pika.exceptions.UnroutableError, tries=3, delay=1, backoff=2)
#     def publish(self, key, msg):
#         try:
#             self.channel.basic_publish(exchange=self.exchange,
#                                        routing_key=key,
#                                        body=json.dumps(msg),
#                                        properties=pika.BasicProperties(content_type='application/json',
#                                                                        delivery_mode=2),
#                                        mandatory=True)
#         except pika.exceptions.UnroutableError:
#             LOG.warning('Message was returned')
