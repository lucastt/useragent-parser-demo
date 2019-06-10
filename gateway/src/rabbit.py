import os
import pika


def _get_channel():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            'rabbit',
            retry_delay=os.environ['retry_delay'],
            connection_attempts=os.environ['CONNECTION_ATTEMPTS']
        )
    )
    channel = connection.channel()
    return channel, connection


def setup():
    channel, connection = _get_channel()
    for index in range(os.environ['SCALE'] + 1):
        channel.queue_declare(queue=str(index))
    connection.close()


# Use decorators to start and end the connection 
def send(message, queue_id='1'):
    channel, connection = _get_channel()
    channel.basic_publish(exchange='',
                          routing_key=queue_id,
                          body=message)
    connection.close()
