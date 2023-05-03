import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='Fogo!!')
channel.queue_declare(queue='Temperatura da CPU')

def callback(ch, method, properties, temperatura):
    print("Recebendo valor de temperatura: ", float(temperatura))
    #Processadores Intel continuam trabalhando de forma segura com temperaturas de até 70 °C
    # 100 °Cé considerado nível perigoso e mecanismos de proteção
    #  como desligamento súbito e redução do clock, podem ser ativados automaticamente
    if (float(temperatura) > 70):
        print("Temperatura alta detectada!")
        channel.basic_publish(exchange='', routing_key='Fogo!!', body="true")

channel.basic_consume(queue='Temperatura da CPU', auto_ack=True, on_message_callback=callback)

print(' Aguardando. Para sair, aperte ctrl c')
channel.start_consuming()

connection.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Encerrado')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)