import pika

def main():
    # Create a connection to the RabbitMQ server running on the local machine
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # Declare queue bindings
    severities = ['eventos_importantes','orcamentos','ordens']    
    
    for severity in severities:
        channel.queue_bind(
            exchange='direct_exchange',
            queue='q4_logs',
            routing_key=severity
            )    

    channel.queue_bind(
            exchange='fanout_exchange',
            queue='q1_informacoes_criticas'
            )
    
    channel.close()