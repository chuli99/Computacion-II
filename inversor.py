import sys,os,argparse
#[pipe]

def main():
    parser = argparse.ArgumentParser(description="Comandos")
    parser.add_argument("-f","--file",type = str,required = True, help ="Directorio del archivo")
    args = parser.parse_args()
    pipes_generator(args.file)

def pipes_generator(file):
    with open(file,'w') as f:
        f.write("Hola Mundo\n"
                   "que tal\n"
                   "ese es un archivo \n"
                   "de ejemplo."
                        )
    s = open(file,"r")       
    list_lines = s.readlines()
    f.close()
    for i in range(len(list_lines)):
        r,w = os.pipe()
        pid = os.fork()    
        if pid:
            os.close(r)
            w = os.fdopen(w,'w')
            w.write(list_lines[i])
            w.close()
            os.wait()
            sys.exit(0)
        else:
            os.close(w)
            r = os.fdopen(r,'r')
            line = r.readline()
            print(f"{line[::-1].strip()}")
            r.close()







main()
