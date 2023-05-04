import pika


def main():
    # Create a connection to the RabbitMQ server running on the local machine
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()

    routing_key_eventos = "eventos_importantes"
    routing_key_ordens = "ordens"
    routing_key_orcamentos = "orcamentos"
    
    queue = "q4_logs"
    exchange_name = "direct_exchange"
    
    
    channel.queue_bind(
        exchange=exchange_name, queue=queue, routing_key=routing_key_eventos
    )
    channel.queue_bind(
        exchange=exchange_name, queue=queue, routing_key=routing_key_ordens
    )
    channel.queue_bind(
        exchange=exchange_name, queue=queue, routing_key=routing_key_orcamentos
    )

    channel.close()
print(" [x] SET" )