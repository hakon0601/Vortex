import SocketServer
import datetime

# Could easily be extended to handle asynchronous calls
class MyTCPHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print datetime.datetime.now()
        print str(self.client_address[0]) + " wrote:"
        print self.data
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "178.62.193.33", 12000

    # Create the server, binding host and port
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you interrupt the program.
    server.serve_forever()
