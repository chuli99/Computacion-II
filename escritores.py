from re import I
import sys
import time
import string
import subprocess 
import os
import argparse
from os import fork

def file_c(args):
    if os.path.exists(args):
        filedirectory = open(f"/home/chuli/Documentos/UM/Computacion-II/{args}.txt","r")
    else:
        filedirectory = open(f"/home/chuli/Documentos/UM/Computacion-II/{args}.txt","w+")  
    filedirectory.close

def list_alphabet():
    alphabet = []
    alphabet = list(string.ascii_uppercase)
    return alphabet

    
def main():
    parser = argparse.ArgumentParser(description="Comandos")
    parser.add_argument("-n", "--number", type=int , required=True , help="Numero de procesos hijos a generar" )
    #parser.add_argument("-h", "--help", action="store_true", help="Mostrar ayuda")
    parser.add_argument("-v", "--verbose", action="store_true", help="Activar modo verbose")
    parser.add_argument("-r", "--repetitions", type=int , required=True, help="Activar modo verbose")
    parser.add_argument("-f", "--file",type=str,required=True)
    args = parser.parse_args()
    fork_generator(args.number,args.verbose,args.repetitions,args.file)
    file_c(args.file)
    os.wait()

def fork_generator(number,verbose,repetitions,file):      
    list_abc = list_alphabet()
    for i in range(number):
        forkp = fork()
        if forkp == 0:
            pid = os.getpid()
            for j in range(repetitions):
                if verbose:
                    print("Proceso",pid,"escribiendo letra",list_abc[i])
                    archivo = open('ejemplo.txt','w')
                    with open(f"/home/chuli/Documentos/UM/Computacion-II/{file}.txt","a") as filedirectory:
                        filedirectory.write(str(list_abc[i]))
                        filedirectory.flush()
                    time.sleep(1)
                else:
                    with open(f"/home/chuli/Documentos/UM/Computacion-II/{file}.txt","a") as filedirectory:
                        filedirectory.write(str(list_abc[i]))
                        filedirectory.flush()
            time.sleep(0.5)
            os._exit(0)    

    #for i in range(number):
        #os.wait()

if __name__ == '__main__':
    main()