import pika
import time
import random
import sys
import os

def main():    
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()   

    exchange_name = "direct_exchange"
    queue_name = "q3_compras"    
    
    channel.exchange_declare(exchange=exchange_name, exchange_type='direct')

    channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key="orcamentos")
    channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key="ordens")
    
    def callback(ch, method, properties, body):
        time.sleep(random.randint(10,20))
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