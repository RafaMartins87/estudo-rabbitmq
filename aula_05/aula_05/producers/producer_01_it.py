import pika
import datetime as dt
import time
import random

# Establish a connection with RabbitMQ server
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

# Create a channel
channel = connection.channel()

categories = ['ERRORS']
priorities = ['ALTA', 'MEDIA', 'BAIXA']
statuses = ['ABERTA', 'ENCERRADA']
department = 'IT'

# Create a message 
for i in range(10_000):
    
    # Assemble message
    category = random.choice(categories)
    priority = random.choice(priorities)
    status = random.choice(statuses)

    time_stamp = dt.datetime.strftime(dt.datetime.now(), format='%Y-%m-%d %H:%M:%S.%f')
    message = f'{time_stamp} {i:6} Mensagem criada por {department} com prioridade {priority} para informar sobre {category}.'

    print(f" [x] Sent {message}")
    time.sleep(random.randint(0,3))
    
    channel.basic_publish(exchange='fanout_exchange', routing_key='it.*.alta.*', body=message)
    
    channel.basic_publish(exchange='topic_exchange', routing_key=f'{department}.{category}.{priority}.{status}', body=message)

# Close the connection
connection.close()

## REGRAS DE ENVIO

## 1. Todos os logs são publicados no modo *fanout*.   
## 2. Todos erros de alta prioridade em aberto são publicados no modo *topic*, rota *department.category.priority.status*.
