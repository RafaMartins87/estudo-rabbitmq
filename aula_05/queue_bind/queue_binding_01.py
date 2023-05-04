import pika


def main():
    # Create a connection to the RabbitMQ server running on the local machine
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()

    # Declare queue bindings
    severity = "it.*.alta.aberta"

    channel.queue_bind(
        exchange="topic_exchange", queue="q1_informacoes_criticas", routing_key=severity
    )

    channel.close()
    print(" [x] SET" )
