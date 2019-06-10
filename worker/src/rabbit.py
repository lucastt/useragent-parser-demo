import pika


def _get_channel():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            'rabbit',
            retry_delay=5,
            connection_attempts=10
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
