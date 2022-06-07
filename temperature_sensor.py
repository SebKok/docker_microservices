from time import time
import pika
import sys
import os
from datetime import datetime
import random
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='temperature')

def main():
    while True:
        time.sleep(1)
        current_temp = 12 + random.uniform(-5.0, 5.0)
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        body=f'{{"timestamp": "{timestamp}", "temperature" : "{current_temp}"}}'

        channel.basic_publish(exchange='',
        routing_key='temperature',
        body=body,
        properties=pika.BasicProperties(
            content_type='application/json',
            content_encoding="UTF-8",
            expiration='600000',
            priority=1,
            app_id="temperature",
            correlation_id="1",
            headers={}
        )
        )
        print(f" [x] Sent {body}")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            connection.close()
            sys.exit(0)
        except SystemExit:
            connection.close()
            os._exit(0)

connection.close()