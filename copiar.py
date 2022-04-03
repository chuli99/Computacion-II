import argparse
from ast import arguments
import os


def main():
    parser = argparse.ArgumentParser(description="Copia de archivos con argparse")
    parser.add_argument("-i",type=str, help = "Archivo que desea buscar")
    parser.add_argument("-o",type=str, help = "Archivo a crear o sobreescribir")
    arguments = parser.parse_args()
    return(arguments)

def file_search(file, newfile):
    try:
        f = open(file,"r")
        read_file = f.read()
        print(read_file)
        f.close()
        cond = True
    except FileNotFoundError:
        print("Archivo no existente, ingresar nuevamente")
        cond = False
    if cond == True:
        n_file = open(newfile + ".txt","w")
        n_file.write(read_file)
        n_file.close()
        with open(newfile + ".txt", "r+")as n_file:
            read_new_f = n_file,read()
            print("Archivo:", newfile, "tiene el siguiente contenido:")
            read_new_f

argumentos = main()
file_search(argumentos.file,argumentos.new_file)