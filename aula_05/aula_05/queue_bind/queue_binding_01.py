import pika

def main():
    # Create a connection to the RabbitMQ server running on the local machine
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    
    channel.queue_bind(
        exchange='fanout_exchange',
        queue='q1_informacoes_criticas'
    )

    channel.close()