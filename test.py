import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='temperature')

channel.basic_publish(exchange='', routing_key='temperature', body='12')
print(" [x] Sent 'Hello World!'")
connection.close()