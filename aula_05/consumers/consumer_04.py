import pika
import time
import random
import sys
import os

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # channel.exchange_declare(exchange='fanout_exchange', exchange_type='fanout')

    # result = channel.queue_declare('', exclusive=True)
    # queue_name = result.method.queue

    # channel.queue_bind(exchange='fanout_exchange', queue=queue_name, routing_key='it.*.alta.*')

    exchange_name_direct = "direct_exchange"
    exchange_name_topic = "topic_exchange"
    exchange_name_fanout = "fanout_exchange"
    
    queue_name = "q4_logs"   
    
    channel.exchange_declare(exchange=exchange_name_direct, exchange_type='direct')
    channel.exchange_declare(exchange=exchange_name_topic, exchange_type='topic')
    channel.exchange_declare(exchange=exchange_name_fanout, exchange_type='fanout')

    channel.queue_bind(exchange=exchange_name_direct, queue=queue_name, routing_key="eventos_importantes")
    channel.queue_bind(exchange=exchange_name_direct, queue=queue_name, routing_key="orcamentos")
    channel.queue_bind(exchange=exchange_name_direct, queue=queue_name, routing_key="ordens")
    
    channel.queue_bind(exchange=exchange_name_topic, queue=queue_name, routing_key="#")
    channel.queue_bind(exchange=exchange_name_fanout, queue=queue_name, routing_key="#")
    
    def callback(ch, method, properties, body):
        time.sleep(random.randint(1,20))
        print(" [x] %r:%r" % (method.routing_key, body))    

    channel.basic_consume(
        queue=queue_name, 
        on_message_callback=callback, 
        auto_ack=True
        )
    
    print(' [*] Waiting for logs. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")

        # Attempt to exit gracefully
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)