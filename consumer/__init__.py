import json
import logging

import pika
import redis


logging.config.fileConfig('logging.ini')
LOG = logging.getLogger(__name__)
REDIS_CONN = None


def callback(channel, method_frame, header_frame, body):
    LOG.info(method_frame.delivery_tag)
    body = json.loads(body)
    transaction_id = body.get('transaction_id')
    redis_obj = channel.redis_conn.get(transaction_id)
    LOG.info(redis_obj)
    LOG.info(body)
    channel.basic_ack(delivery_tag=method_frame.delivery_tag)


def create_consumer(app_settings, workers, queue):
    redis_connector = redis.Redis(host=app_settings.REDIS_HOST, port=app_settings.REDIS_PORT, db=0)
    while True:
        try:
            # Colocar também número de worker
            LOG.info(f'Inicializando {workers} consumers para fila {queue}')
            # Shuffle the hosts list before reconnecting.
            # This can help balance connections.
            # random.shuffle(all_endpoints)
            # connection = pika.BlockingConnection(all_endpoints)
            credentials = pika.PlainCredentials(app_settings.RABBIT_USER, app_settings.RABBIT_PASS)

            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=app_settings.RABBIT_HOST, credentials=credentials))
            channel = connection.channel()
            channel.basic_qos(prefetch_count=1)
            ## This queue is intentionally non-durable. See http://www.rabbitmq.com/ha.html#non-mirrored-queue-behavior-on-node-failure
            ## to learn more.
            channel.exchange_declare(exchange='teste_ex', exchange_type='direct')
            channel.queue_declare(queue=queue, durable=True)
            channel.queue_bind(queue=queue, exchange='teste_ex', routing_key='teste_key')

            channel.redis_conn = redis_connector
            channel.basic_consume(queue=queue, on_message_callback=callback)
            try:
                channel.start_consuming()
            except KeyboardInterrupt:
                channel.stop_consuming()
                connection.close()
                break
        except pika.exceptions.ConnectionClosedByBroker:
            # Uncomment this to make the example not attempt recovery
            # from server-initiated connection closure, including
            # when the node is stopped cleanly
            #
            # break
            continue
            # Do not recover on channel errors
        except pika.exceptions.AMQPChannelError as err:
            LOG.info("Caught a channel error: {}, stopping...".format(err))
            break
            # Recover on all other connection errors
        except pika.exceptions.AMQPConnectionError:
            LOG.info("Connection was closed, retrying...")
            continue
