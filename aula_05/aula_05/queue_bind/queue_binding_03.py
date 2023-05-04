import pika

def main():
    # Create a connection to the RabbitMQ server running on the local machine
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # Declare queue bindings
    severities = ['orcamentos','ordens']    
    
    for severity in severities:
        channel.queue_bind(
            exchange='direct_exchange',
            queue='q3_compras',
            routing_key=severity
    )    

    channel.close()