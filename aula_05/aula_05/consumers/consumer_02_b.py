import pika
import time
import random

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))

time.sleep(random.randint(2,4))

channel.basic_consume(
    queue='q2_participacao_obrigatoria_b', on_message_callback=callback, auto_ack=True
    )

channel.start_consuming()