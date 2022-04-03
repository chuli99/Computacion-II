import getopt
import sys
from unittest import result
def calc():
    args = sys.argv[1:]
    comandos = "o:n:m:"

    (comandos, arg) = getopt.getopt(args,comandos)
    operation = None
    n = None 
    m = None 
    for op,ar in comandos:
        if op in ['-o']:
            operation = ar
        elif op in['-n']:
            n = int(ar)
        elif op in['-m']:
            m = int(ar)
    
    if operation == '+':
        result = (n + m)
    elif operation == '-':
        result = (n - m)
    elif operation == '*':
        result = (n * m)
    elif operation == '/':
        result = (n / m)
    else:
        print("Operacion incorrecta")
    print("El resultado es:",result)
calc()