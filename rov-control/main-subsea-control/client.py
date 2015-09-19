#!/usr/bin/env python
import socket
import serial
from time import sleep


def main():

	try:
		msg = "Hello, World!"

#		tcp_ip = '192.168.1.45'
		tcp_port = 5010
		buffer_size = 1024

		s = initialize_socket()
#		s.connect((tcp_ip, tcp_port))

		s.open_socket(('192.168.1.45', tcp_port))

		s.send('I am alive!')
		
		
		#sets up a serial interface to the arduino mega
		ser = serial.Serial('/dev/ttyACM0',9600)
		
		while True:
			data = s.recv(buffer_size)
			print_debuginfo("Topsite:"+ data)
			write_arduino(ser,data)
			print_debuginfo('write complete: '+data)
			msg_from_arduino = read_arduino(ser) # looks like there is a error in here
			print_debuginfo('read complete: '+ msg_from_arduino) 
			s.send('Hei'+ msg_from_arduino)
			print_debuginfo('send complete')

	except Exception, e:
		print_error('Error in main: ' + str(e))
	finally:
		s.close()
		print_warning('Closing socket')
		
def initialize_socket():
	return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class Colour:
    header = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    warning = '\033[93m'
    error = '\033[91m'
    end_colour = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

def read_arduino(serial_name):
	string = 'Arduino:'
#	while (serial_name.inWaiting()):
	temp = serial_name.read()
#		if (temp != '\n' and temp != '\r'):
	string  += temp

	mesage_from_arduino = string 
	return mesage_from_arduino

def write_arduino(serial_name, message_to_arduino):
	serial_name.write(message_to_arduino)

def print_debuginfo(msg):
	print Colour.blue + msg +Colour.end_colour

def print_warning(msg):
	print Colour.warning + msg + Colour.end_colour  	

def print_error(msg):
	print Colour.error + msg + Colour.end_colour

def print_header(msg):
	print Colour.error + msg + Colour.end_colour

if __name__ == '__main__':
    main()
