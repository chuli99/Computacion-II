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