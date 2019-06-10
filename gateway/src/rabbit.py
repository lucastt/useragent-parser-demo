import os
import pika


def _get_channel():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            'rabbit',
            retry_delay=int(os.environ['RETRY_DELAY']),
            connection_attempts=int(os.environ['CONNECTION_ATTEMPTS'])
        )
    )
    channel = connection.channel()
    return channel, connection


def setup():
    channel, connection = _get_channel()
    for index in range(int(os.environ['SCALE']) + 1):
        channel.queue_declare(queue=str(index))
    connection.close()


# Use decorators to start and end the connection 
def send(queue_id, message):
    channel, connection = _get_channel()
    channel.basic_publish(exchange='',
                          routing_key=queue_id,
                          body=message)
    connection.close()
