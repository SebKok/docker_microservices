import pika
import random

# credentials = pika.credentials.PlainCredentials('user', 'password')
# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=credentials))
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='temperature')

current_temp = 12 + random.randint(-2, 2)
channel.basic_publish(exchange='',
routing_key='temperature',
body=f'Temperature read: {current_temp}',
properties=pika.BasicProperties(
    content_type='application/json',
    expiration='600000',
    priority=1,
    app_id="temperature",
    reply_to="n/a"
)
)
print(f" [x] Sent {current_temp}")

connection.close()