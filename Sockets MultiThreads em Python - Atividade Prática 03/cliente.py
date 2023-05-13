#Natália Ribeiro de Almada
#Importa os seuints módulos de (biblioteca padrão.
#socket, threading, time, psutil e matplotlib.pyplot 
import socket
import threading
import pytime as time
import psutil
import matplotlib.pyplot as plt

#Define a função que envia uma mensagem de tamanho específico para o server
def attack_server(message, num_requests):
    start_time = time.time()
    for i in range(num_requests):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 5000))
        client_socket.send(message.encode())
        response = client_socket.recv(1024)
        client_socket.close()
    end_time = time.time()
    # calcula o tempo que leva entre eviar e receber as respostas.
    return end_time - start_time

message_sizes = [1, 512, 1024, 4096]
num_requests = 1000

cpu_usage = []
memory_usage = []
network_usage = []

for message_size in message_sizes:
    message = 'A' * message_size
    time_taken = attack_server(message, num_requests)
    cpu_usage.append(psutil.cpu_percent())
    memory_usage.append(psutil.virtual_memory().percent)
    network_usage.append(psutil.net_io_counters().bytes_sent)

plt.figure(figsize=(10, 8))
plt.subplot(311)
plt.plot(message_sizes, cpu_usage)
plt.title('CPU Usage')
plt.xlabel('Message Size (bytes)')
plt.ylabel('Usage (%)')
plt.subplot(312)
plt.plot(message_sizes, memory_usage)
plt.title('Memory Usage')
plt.xlabel('Message Size (bytes)')
plt.ylabel('Usage (%)')
plt.subplot(313)
plt.plot(message_sizes, network_usage)
plt.title('Network Usage')
plt.xlabel('Message Size (bytes)')
plt.ylabel('Bytes Sent')
plt.tight_layout()
plt.show()
