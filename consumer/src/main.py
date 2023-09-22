import asyncio

import pika
from pika import BlockingConnection

credentials = pika.PlainCredentials('admin', 'pass')

connection = BlockingConnection(
    parameters=pika.ConnectionParameters(
        host='rabbitmqServer', credentials=credentials
    )
)

channel = connection.channel() # start a channel
channel.queue_declare(queue='task_queue', durable=True) # Declare a queue


def callback(channel, method, properties, body):
    print(f'Consumed message {body.decode()} from queue')


async def consumer():
    channel = connection.channel()
    channel.basic_consume('task_queue', on_message_callback=callback)
    channel.start_consuming()

if __name__ == '__main__':
    asyncio.run(consumer())
