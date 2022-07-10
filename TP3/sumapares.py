import sys
import time
import subprocess as sp
import os
import argparse
from os import fork

def main():
    parser = argparse.ArgumentParser(description="Comandos")
    parser.add_argument("-n", "--number", type=int , required=True , help="Numero de procesos hijos a generar" )
    #parser.add_argument("-h", "--help", action="store_true", help="Mostrar ayuda")
    parser.add_argument("-v", "--verbose", action="store_true", help="Activar modo verbose")
    args = parser.parse_args()
    fork_generator(args.number,args.verbose)
    os.wait()

def fork_generator(number,verbose):
    for i in range(number):
        forkp = fork()
        #type_process = os.fork()
        if forkp == 0:
            pid = os.getpid()
            suma = 0
            ppid = os.getppid()
            if verbose:
                print("Proceso iniciado ",pid)
                #time.sleep(1)
                for k in range (0, pid+1, 2):
                    suma = k + suma
                time.sleep(0.5)
                print("Proceso terminado ",pid)
                print(pid,"-",ppid,":",suma)
            
            os._exit(0)

if __name__ == '__main__':
    main()

