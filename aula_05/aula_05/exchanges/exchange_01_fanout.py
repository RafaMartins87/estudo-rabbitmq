import pika

# Establish a connection with RabbitMQ server
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

# Create a channel
channel = connection.channel()

# Define exchange name and routing keys
exchange_name = 'fanout_exchange'

# Declare exchange
channel.exchange_declare(
    exchange=exchange_name, exchange_type='fanout'
)

channel.close()