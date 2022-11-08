import calc
import argparse, time, os,math

def main():
    global pool,args,lines,results
    
    parser = argparse.ArgumentParser(description="Comandos")
    parser.add_argument("-f","--file",required=True,help="Archivo a procesar")
    parser.add_argument("-c","--calculate",required=True,help="Operacion a realizar")
    args = parser.parse_args()
    
    lines = []
    results = []

    read_lines(args.file)
    calculate_function(args.calculate)
    


def read_lines(file):
    #Abro txt y leo linea por linea y almaceno en una lista
    with open(file) as f:
        global lines
        for line in f:
            strip_lines = line.strip('')
            listli = strip_lines.split()
            print(listli)
            #Convierto la lista a valores enteros
            for i in range(len(listli)):
                listli[i] = int(listli[i])
            m = lines.append(listli)            
            
            
def calculate_function(calculate):
    matriz_resultado = []
    #Ejecuta lo ingresado por consola en -c
    for i in range(len(lines)):
        if calculate == "root":
            resultado = calc.raiz_cuadrada.delay(lines[i])
            #Almacena lo el calculo realizado por funcion raiz:
            resultado = resultado.get()
            #esultado.append(matriz_resultado)  
        
        elif calculate == "pow":
            resultado = calc.potencia.delay(lines[i])
            #Almacena lo el calculo realizado por funcion raiz:
            resultado = resultado.get()
            #resultado.append(matriz_resultado)  
        
        elif args.calculate == "log":
            resultado = calc.logaritmo.delay(lines[i])
            #Almacena lo el calculo realizado por funcion raiz:
            resultado = resultado.get()
            #resultado.append(matriz_resultado)  
    print("Calculo realizado con exito")

if __name__ == "__main__":
    main()