from multiprocessing import Queue
#from queue import Queue
import os,sys,threading,codecs


def thread_function1(queue1,queue2):
    print("Hilo 1")
    #stdin para leer
    sys.stdin = open(0)
    print("Ingrese una linea:")
    line = sys.stdin.readline()
    #Hilo 1 agrega mensaje a la queue
    queue1.put(line)
    #Hilo 1 lee mensaje encriptado de la cola
    line_codec = queue2.get()
    print(f"Hilo 1 recibe mensaje encriptado:{line_codec}")

def thread_function2(queue1,queue2):
    data = queue1.get()
    print(f"Hilo 2 recibe mensaje: {data}")
    line_codec = Rot_13(data)
    print("Hilo 2 almacena mensaje encriptado..")
    queue2.put(line_codec)

def Rot_13(line):
    line_codec = codecs.encode(line,'rot_13')
    return line_codec

if __name__ == '__main__':
    q1 = Queue()
    q2 = Queue()
    t1 = threading.Thread(target = thread_function1,args=(q1,q2), daemon = True)    
    #t1.join()
    t2 = threading.Thread(target = thread_function2,args=(q1,q2), daemon = True)
    t1.start()
    #t1.join()
    t2.start()
    t1.join()
    t2.join()
