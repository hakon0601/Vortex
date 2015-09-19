import time
from socket import *
import sys
import os
from Communication import tcpclient

print tcp_client

delay = sys.stdin.readline().split(' ')[0]
print "delay is: " + delay

print "Establishing connnection"
socket = tcp_client.open_socket()

print "Sending data"
for line in sys.stdin:
    send_and_receive(msg, socket)
    time.sleep(float(delay))

tcp_client.close()

