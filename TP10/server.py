import socketserver,subprocess
import signal,os,argparse


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            self.data = self.request.recv(1024).strip()
            pp = subprocess.Popen([self.data], stdout = subprocess.PIPE,stderr = subprocess.PIPE, shell = True)
            out,err = pp.communicate()
            if str(self.data) == "":
                server.shutdown()
                exit(0)
            if err:
                self.request.sendall(b"ERROR \n"+err)
                print(err)
            else:
                self.request.sendall(b"OK\n"+out)
                print(out)
            
            print("PID: %d" % os.getpid())
            #signal.pause()

#Hereda para concurrencia
class ProcTCPServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass

class ThrTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Comandos")
    parser.add_argument("-p","--port", type=int,required=True,help="Numero de puerto del servidor")
    parser.add_argument("-c","--concurrence", type=str ,required=True,help="P o T dependiendo de un proceso o un hilo")
    args = parser.parse_args()
    HOST, PORT = "localhost", args.port
    print(HOST,PORT)
    socketserver.TCPServer.allow_reuse_address = True
    # Create the server, binding to localhost on port 9999
    
    if args.concurrence == 'p':
        with ProcTCPServer((HOST, PORT), MyTCPHandler) as server:
            server.serve_forever()
            try:
                signal.pause()
            except:
                server.shutdown()
            #server.shutdown()

    if args.concurrence == 't':
        with ThrTCPServer((HOST, PORT), MyTCPHandler) as server:
            server.serve_forever()
            try:
                signal.pause()
            except:
                server.shutdown()
            #server.shutdown()
