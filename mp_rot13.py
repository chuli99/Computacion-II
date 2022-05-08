from multiprocessing import Process,Pipe
import os,time,sys,codecs
import _multiprocessing as mp

def child1(arg):
    
    #stdin para leer
    sys.stdin = open(0)
    print("Ingrese una linea:")
    line = sys.stdin.readline()
    arg.send(line)
    print("Hijo 1 lee:",line)
    
    #print("id hijo1:",os.getppid(),"id padre",os.getpid())
    time.sleep(5)
    #os.system("ps ft")
    #print("F")

def child2(arg):
    
    print("id hijo2:",os.getppid(),"id padre:",os.getpid())
    print("Hijo 2 lee:")
    line = str(arg.recv())
    print(line)
    #Hijo 2 aplica Rot13
    line_codec = codecs.encode(line,'rot_13')
    print(line_codec)

if __name__ == "__main__":
    a,b = Pipe()
    print("Parent Id",os.getpid())
    p1 = Process(target=child1, args=(a,))
    p1.run()
    p2 = Process(target=child2, args= (b,))    
    p2.run()
