import pika
import random

def main():
    # Create a connection to the RabbitMQ server running on the local machine
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # Declare queue bindings
    severities = ['orcamentos','ordens','eventos_importante']
    severity = random.choice(severities)
    
    queue_list = [
        'q2_participacao_obrigatoria_a',
        'q2_participacao_obrigatoria_b',
        'q2_participacao_obrigatoria_c',
        'q2_participacao_obrigatoria_d'
        ]

    for queue in queue_list:        
        channel.queue_bind(
            exchange='direct_exchange',
            queue=queue,
            routing_key=severity
        )

    channel.close()