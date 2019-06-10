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


# Use decorators to start and end the connection 
def consume(queue_id, callback):
    channel, _ = _get_channel()
    channel.basic_consume(queue=queue_id,
                          auto_ack=True,
                          on_message_callback=callback)
    channel.start_consuming()
