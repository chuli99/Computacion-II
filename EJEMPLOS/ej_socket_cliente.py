#ENUNCIADO CLASE
#Crear un server de mayusculas que atienda a varios clientes simultaneamente usando multiprocessing y/o threading.
#Usar sockets TCP.
#El servidor debe generar un proceso/hilo para atender aun cliente individual
#El cliente debe poder enviar una palabra, el servidor respondera con la mayuscula de esa palabra.
#Si el cliente envia un exit termina, y hace que el proceso/hilo que lo atendia del lado del server tambien termine


import socket

#Importamos si porque usamos los argumentos de linea de comandos cual es el host al que quiero conectarme
import sys

try:
    #Creo el socket, es decir, la estructura de memoria para intercambiar datos con otro nodo. Permite interactuar con ese tcp/ip
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Fallo al crear socket')
    sys.exit()

#Paso los argumentos con host y el port
host = sys.argv[1]
port = int(sys.argv[2])


s.connect((host,port))

while(1) :
    msg = input('Ingrese mensaje a enviar:')
    #envia el msje al socket
    s.send(msg.encode('ascii'))

    #se queda esperando una respuesta
    msg = s.recv(1024)
    
    print('Server reply: '+ msg.decode("ascii"))