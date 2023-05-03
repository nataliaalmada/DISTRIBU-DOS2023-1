import pika 
from playsound import playsound

# Cria uma conexão com o servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

# Cria um canal de comunicação com o servidor RabbitMQ
channel = connection.channel()

# Declara a fila de mensagens no RabbitMQ
channel.queue_declare(queue='Fogo!!')

# Função que será chamada para processar cada mensagem recebida
def callback(ch, method, properties, temperature):
    print("Alerta de Incêndio Ativado!")
    playsound('emergency_alert.mp3')

channel.basic_consume(queue='Fogo!!', auto_ack=True, on_message_callback=callback)

print(' Aguardando. Para sair, aperte ctrl c')#comando crasha o programa
channel.start_consuming()

connection.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Encerrado!')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)