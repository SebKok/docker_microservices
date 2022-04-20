import pika
import random

credentials = pika.credentials.PlainCredentials('user', 'password')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='temperature')

current_temp = 12 + random.randint(-2, 2)
channel.basic_publish(exchange='',
routing_key='temperature',
body=f'Temperature read: {current_temp}')
print(f" [x] Sent {current_temp}")

connection.close()