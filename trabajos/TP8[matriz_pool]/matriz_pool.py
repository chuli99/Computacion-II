import argparse
import os
import time 
import math
from multiprocessing import Pool
import numpy as np

def main():
    global pool,args,lines,results
    
    parser = argparse.ArgumentParser(description="Comandos")
    parser.add_argument("-f","--file",type=str,required=False,help="File")
    parser.add_argument("-p","--process",type=int,required=False,help="Number of process")
    parser.add_argument("-c","--calculate",type=str,required=False,help="Operation")
    args = parser.parse_args()
    
    lines = []
    results = []
    #pool con n procesos
    pool = Pool(processes=args.process)
    read_lines(args)
    calculate_function(args)

def read_lines(args):
    #Abro txt y leo linea por linea y almaceno en una lista
    with open(args.file) as file:
        global lines
        for line in file:
            strip_lines = line.strip('')
            listli = strip_lines.split()
            print(listli)
            #Convierto la lista a valores enteros
            for i in range(len(listli)):
                listli[i] = int(listli[i])
            time.sleep(1)
            m = lines.append(listli)            
            
                
            
        

def calculate_function(calculate):
    #Ejecuta lo ingresado por consola en -c
    for i in range(len(lines)):
        if args.calculate == "root":
            print("Calculando raiz\n")
            result = pool.map(raiz,lines[i])
            #Almacena lo el calculo realizado por funcion raiz:
            results.append(result)  
        elif args.calculate == "pow":
            print("Calculando potencia\n")
            result = pool.map(result)
            #Almacena lo el calculo realizado por funcion potencia:
            results.append(result)
        elif args.calculate == "log":
            print("Calculando logaritmo\n")
            result = pool.map(logaritmo,lines[i])
            #Almacena lo el calculo realizado por funcion logaritmo:
            results.append(result)  
    pool.close()
    #Muestro la matriz resultado
    print("Matriz resultado:\n")
    matriz = np.array(results)
    print(matriz)
    print("\n")

#Funcion que calcula raiz de la lista con elementos de matiz.txt
def raiz(num):
    time.sleep(1)    
    print("Calculando raiz de: ",num," Proceso: ",os.getpid())
    return math.sqrt(num)


#Funcion que calcula potencia de la lista con elementos de matiz.txt
def potencia(num):
    time.sleep(1)
    print("Calculando potencia de: ",num," Proceso: ",os.getpid())
    return math.pow(num,num)

#Funcion que calcula logaritmo de la lista con elementos de matiz.txt
def logaritmo(num):
    time.sleep(1)
    print("Calculando logaritmo de: ",num," Proceso: ",os.getpid())
    return math.log10(num)

if __name__=="__main__":
    main()