#CREAR SERVIDOR PARA QUE UN CLIENTE PUEDA CONECTARSE   
import socket, sys, time

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
"""
socket.socket(FamiliaProtocolos, TipoSocket)
    FamiliaProtocolos: AF_INET / AF_UNIX
    TipoSocket: SOCK_DGRAM - socket datagrama (UDP)
                SOCK_STREAM - socket de flujo (TCP)
"""


# get local machine name
#host = socket.gethostname()                           
host = ""
"""
    el socket atiende en todas las IP's locales: 0.0.0.0
        ej. 127.0.0.1, 192.168.0.10, 10.0.0.1, ...
"""
port = int(sys.argv[1])

# bind to the port
serversocket.bind((host, port))                                  

#Mientras se esta realizando una conexion, los siguientes procesos se almacenan en una cola. 
#En este caso solo 5 pueden estar en la cola para realizar una conexion. 
serversocket.listen(5)

#El accept queda esperando conexiones, es decir un connect de parte del cliente
clientsocket, addr = serversocket.accept()

while True:
    data = serversocket.recvfrom(1024)
    print("Address: %s " % str(addr))
    #print("Address: %s - Port %d" % (address, port))
    print("Recibido: "+data.decode("ascii"))
    msg = input('Enter message to send : ')
    clientsocket.send(msg.encode('ascii'))
    #time.sleep(1)


clientsocket.close()


"""
Conectar al cliente usando ncat:
    ncat 127.0.0.1 1234 -u -v
"""

