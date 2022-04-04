from inspect import ArgSpec
import os
import argparse

def main():
    parser = argparse.ArgumentParser(description="Comandos")
    parser = argparse.ArgumentParser(description=False)
    parser.add_argument("-n", type=int,help="Numero de procesos hijos a generar")
    parser.add_argument("-h", type=str, help="Mostrar ayuda")
    parser.add_argument("-v", type=str, help="Activar modo verbose")
    args = parser.parse_args()
    fork_generator(args)

def fork_generator(args):
    for i in(args.n):
        type_process = os.fork()
        if type_process == 0:
            print("Proceso creado")
            os.exit(0)
