from multiprocessing import Process,Pipe,Queue
import os,time,sys,codecs

def child1(p,q):

    #stdin para leer
    sys.stdin = open(0)
    print("Ingrese una linea:")
    line = sys.stdin.readline()
    p.send(line)
    p.close()
    print("Hijo 1 lee:",line)
    time.sleep(2)
    #Hijo 1 recibe mensaje encriptado de cola de mensajes 
    line_codec = q.get()
    print("Hijo 1 lee mensaje encriptado:",line_codec)
    
def child2(p,q):
    line = str(p.recv())
    print("Hijo 2 lee:",line)
    time.sleep(2)
    #Hijo 2 aplica Rot13
    line_codec = codecs.encode(line,'rot_13')
    #Hijo 2 agrega el mensaje encriptado a la cola de mensajes
    q.put(line_codec)

if __name__ == "__main__":
    a,b = Pipe()
    q = Queue()
    p1 = Process(target=child1, args=(a,q))
    p2 = Process(target=child2, args= (b,q))    
    p1.start()
    p2.start()
    p1.join()
    p2.join()