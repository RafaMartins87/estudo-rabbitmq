import pika


def main():
    # Create a connection to the RabbitMQ server running on the local machine
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()

    # Declare queue bindings
    routing_key = "eventos_importantes"

    queue_a = "q2_participacao_obrigatoria_a"
    queue_b = "q2_participacao_obrigatoria_b"
    queue_c = "q2_participacao_obrigatoria_c"
    queue_d = "q2_participacao_obrigatoria_d"

    channel.queue_bind(exchange="direct_exchange", queue=queue_a, routing_key=routing_key)
    channel.queue_bind(exchange="direct_exchange", queue=queue_b, routing_key=routing_key)
    channel.queue_bind(exchange="direct_exchange", queue=queue_c, routing_key=routing_key)
    channel.queue_bind(exchange="direct_exchange", queue=queue_d, routing_key=routing_key)

    channel.close()
print(" [x] SET" )