import pika


def main():
    # Create a connection to the RabbitMQ server running on the local machine
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()
    
    routing_key_orcamentos = "orcamentos"
    routing_key_ordens = "ordens"
    
    exchange_name = "direct_exchange"
    queue = "q3_compras"

    channel.queue_bind(
        exchange=exchange_name, queue=queue, routing_key=routing_key_orcamentos
    )

    channel.queue_bind(
        exchange=exchange_name, queue=queue, routing_key=routing_key_ordens
    )

    channel.close()
print(" [x] SET" )