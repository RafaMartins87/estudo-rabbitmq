import pika

# 1. Estabelecendo uma conexão com o servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

queue_name_list = [
    'q1_informacoes_criticas',
    'q2_participacao_obrigatoria_a',
    'q2_participacao_obrigatoria_b',
    'q2_participacao_obrigatoria_c',
    'q2_participacao_obrigatoria_d',
    'q3_compras',
    'q4_logs'
    ]

# 2. Criando as filas
for queue in queue_name_list:    
    channel.queue_declare(queue=queue, durable=True)

channel.close()
print(" [x] SET" )