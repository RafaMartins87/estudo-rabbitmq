import pika
import time
import random

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# channel.exchange_declare(exchange='fanout_exchange', exchange_type='fanout')

# result = channel.queue_declare('', exclusive=True)
# queue_name = result.method.queue

# channel.queue_bind(exchange='fanout_exchange', queue=queue_name, routing_key='it.*.alta.*')

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))

time.sleep(random.randint(10,20))

channel.basic_consume(
    queue='q3_compras', on_message_callback=callback, auto_ack=True)

channel.start_consuming()