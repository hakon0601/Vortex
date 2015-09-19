# Echo client program
import socket
import sys

class TCPClient():
    def __init__(self, remote_host_address, port):
        self.host = remote_host_address
        self.port = port

    def open_socket(self):
        for res in socket.getaddrinfo(self.host, self.port, socket.AF_UNSPEC, socket.SOCK_STREAM):
            af, socktype, proto, canonname, sa = res
            try:
                s = socket.socket(af, socktype, proto)
            except socket.error as msg:
                s = None
                continue
            try:
                s.connect(sa)
            except socket.error as msg:
                s.close()
                s = None
                continue
            return s
        if s is None:
            print 'could not open socket'
            return None

    def send(self, message):
        s = self.open_socket()
        if s:
            s.sendall(message)
            s.close()

    def send_and_receive(self, message):
        s = self.open_socket()
        if s:
            s.sendall(message)
            self.receive(s)
            s.close()

    def receive(self, s):
        if s:
            data = s.recv(1024)
            print 'Received', repr(data)
