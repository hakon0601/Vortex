
import socket
import sys

# Create a TCP/IC socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_adress = ('localhost',10000)
print ('starting up on %s port %s' % server_adress , file=sys.stderr)
sock.bind(server_adress)

#listen for incoming connections
sock.listen(1)

while True:
        # wait for a connection
        print ('waiting for connection', file=sys.stderr)
        connection, client_address = sock.accept()

        try:
            print ('connection from', client_address, file=sys.stderr)

            #receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(20)
                print ('received "%s"' % data, file=sys.stderr)

                if data:
                    print ('sending data back to client', file=sys.stderr)
                    connection.sendall(data)
                else:
                    print ('no more data from' , client_address, file=sys.stderr)
                    break

        finally:
            #clean up the connection
            connection.close()
