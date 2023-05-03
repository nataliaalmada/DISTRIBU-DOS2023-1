import pika
import time
import psutil

#cria a função que "sente" atemperatura da cpu
def remetente():
  while True:
    temperatura = psutil.sendordetemp().coretemp[0].current
    channel.basic_publish(exchange='', routing_key='Temperatura da CPU', body=str(temperatura))
    time.sleep(5)
# Cria uma conexão com o servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# Cria um canal de comunicação com o servidor RabbitMQ
channel = connection.channel()
# Declara a fila de mensagens no RabbitMQ
channel.queue_declare(queue='Temperatura da CPU')
#manda a mensagem informando a temperatura
remetente()

connection.close()