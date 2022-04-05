#from inspect import ArgSpec
import sys
import time
import subprocess as sp
import os
import argparse
from os import fork
#from pty import fork

def main():
    parser = argparse.ArgumentParser(description="Comandos")
    parser = argparse.ArgumentParser(description=False)
    parser.add_argument("-n", type=int,help="Numero de procesos hijos a generar")
    #parser.add_argument("-h", type=str, help="Mostrar ayuda")
    parser.add_argument("-v", action="stare_true", help="Activar modo verbose")
    args = parser.parse_args()
    fork_generator(args.n,args.v)
    os.wait()

def fork_generator(args,verbose):
    for i in(args):
        type_process = os.fork()
        if type_process == 0:
            pid = os.getpid()
            suma = 0
            ppid = os.getppid()
            print("Proceso iniciado ",pid)
            if verbose:
                print("Proceso iniciado ",pid)
            for k in range (0, pid+1, 2):
                suma = k + suma
            if verbose:
                print("Ending process ",pid)
            print(pid, ppid, suma)
            os.exit(0)
            
            
            
            os._exit(0)
        
if __name__ == '__main__':
    main()

