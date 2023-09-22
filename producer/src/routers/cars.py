import pika
from fastapi import APIRouter

router = APIRouter(
    prefix="/cars",
    tags=["cars"]
)

credentials = pika.PlainCredentials('admin', 'pass')

connection = pika.BlockingConnection(
    pika.ConnectionParameters("rabbitmqServer",
                              credentials=credentials)
)
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)


@router.get("/",)
async def read_cars():
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=b"hello it's published message",
        properties=pika.BasicProperties(delivery_mode=2)
    )
    return [
        {"name": "Aston Martin Vulcan"},
        {"name": "Bugatti Chiron"}
    ]
