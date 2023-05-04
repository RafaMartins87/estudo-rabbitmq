import pika
import datetime as dt
import time
import random

# Establish a connection with RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

# Create a channel
channel = connection.channel()

categories = ["evento", "movimentacao"]
priorities = ["alta", "media", "baixa"]
# statuses = ['aberta', 'encerrada']
department = "rh"

# Create a message
for i in range(10_000):
    # Assemble message
    category = random.choice(categories)
    priority = random.choice(priorities)
    # status = random.choice(statuses)

    time_stamp = dt.datetime.strftime(dt.datetime.now(), format="%Y-%m-%d %H:%M:%S.%f")
    message = f"{time_stamp} {i:6} Mensagem criada por {department} com prioridade {priority} para informar sobre {category}."

    print(f" [x] Sent {message}")
    time.sleep(random.randint(0, 3))

    if priority == "ALTA":
        channel.basic_publish(
            exchange="direct_exchange", routing_key="eventos_importantes", body=message
        )

    channel.basic_publish(
        exchange="topic_exchange",
        routing_key=f'{department}.{priority}.{category}',
        body=message,
    )

    channel.basic_publish(exchange="fanout_exchange", routing_key="mkt.*", body=message)

# Close the connection
connection.close()

## REGRAS DE ENVIO
## 1. Todos os eventos são publicados no modo *fanout*.
## 2. Eventos importantes (prioridade alta) são publicados no modo *direct*, rota *eventos_importantes*.
## 3. Todas as movimentações são publicadas no modo *topic*, rota *department.category.priority*.
