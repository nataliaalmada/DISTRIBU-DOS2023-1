#Natália Ribeiro de Almada
#Importa os módulos socket e threading da biblioteca padrão.
import socket
import threading

#Define a função que recebe o objeto client_socket,representando
# o socket da conexão estabelecida com o cliente. 
 
 
# Em seguida, fecha a conexão.
def handle_client(client_socket):
    #recebe a mensagem do cliente
    request = client_socket.recv(1024)
    #inverte  a ordem dos caracteres e envia a mensagem de volta ao cliente.
    response = request[::-1]
    client_socket.send(response)
    client_socket.close()
 
 #cria o socket que vai utilizara família de protocolos AF_INET (IPv4) 
 # e o protocolo de transporte SOCK_STREAM (TCP).
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Associa o socket do servidor à interface de rede com endereço IP 0.0.0.0 e à porta 5000.
server_socket.bind(('0.0.0.0', 5000))
#põe o socket do servidor em "modo de escuta" para aguardar novas conexões.
server_socket.listen()

#Entra em loop  para aguardar novas conexões. 

#  A thread executa a função handle_client, 
while True:
    #argumento do socket da conexão 
    client_socket, address = server_socket.accept()
    # Quando estaelece conexão, é criada uma nova thread para lidar com ela.
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    #xomeça a thread
    client_thread.start()
