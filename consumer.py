import pika, sys, os

def main():
    credentials = pika.credentials.PlainCredentials('user', 'password')
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='temperature')

    def callback(ch, method, propoerties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(queue='temperature', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)