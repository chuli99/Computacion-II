import getopt
import sys
args = sys.argv[1:]

comandos = ['o:n:m:']

oplist, args = getopt.getopt(args,comandos)

print(oplist)
print(args)