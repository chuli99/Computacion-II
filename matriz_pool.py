# Realizar un programa en python que reciba por argumentos:

# -p cantidad_procesos
# -f /ruta/al/archivo_matriz.txt
# -c funcion_calculo
# El programa deberá leer una matriz almacenada en el archivo de texto pasado por argumento -f, y deberá calcular la funcion_calculo para cada uno de sus elementos.
# Para aumentar la performance, el programa utilizará un Pool de procesos, y cada proceso del pool realizará los cálculos sobre una de las filas de la matriz.
# La funcion_calculo podrá ser una de las siguientes:
# raiz: calcula la raíz cuadrada del elemento.
# pot: calcula la potencia del elemento elevado a si mismo.
# log: calcula el logaritmo decimal de cada elemento.
# Ejemplo de uso:
# Suponiendo que el archivo /tmp/matriz.txt tenga este contenido:
# 1, 2, 3
# 4, 5, 6
# python3 calculo_matriz -f /tmp/matriz.txt -p 4 -c pot
# 1, 4, 9
# 16, 25, 36

import argparse
import os
from multiprocessing import Pool

def main():
    parser = argparse.ArgumentParser(description="Comandos")
    parser.add_argument("-f","--file",type=str,required=False,help="file")
    parser.add_argument("-p","--process",type=int,required=True,help="Number of process")
    parser.add_argument("-c","--calculate",type=str,required=False,help="Operation")
    args = parser.parse_args()
    pool = Pool(processes=args.process)
    lista = openFile(args.file)
    result = pool.map(funcion_calculo, lista)
    print(result)

def openFile(file):
    matrix=[]
    with open(file, 'r') as f:
        for line in f.readlines():
            matrix.append(list(line.strip().replace(",","").replace(" ", "")))
    return matrix

def funcion_calculo(row):
    result=[]
    for num in row:
        num=int(num)
        result.append(num*num)
    return result


if __name__=="__main__":
    main()