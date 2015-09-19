#!/usr/bin/env python
import serial
from time import sleep
from os import system

def main ():
	print('start')
	#this did not work realy well. 
	#system('stty -F  /dev/ttyACM0 -hupcl')
	#sleep(0.2)
	ser = serial.Serial('/dev/ttyUSB0', 9600)
	

	#Arduino resets on serial start and has a built in delay for programing therfore the sleep 
	sleep(1)
	#worked as a solution to siable dtr:  stty -F /dev/ttyACM0 -hupcl
	
	while True:
		msg = 'hei paa deg'
		msg_from_arduino = ''
		write_arduino(ser, msg)
		print('reading from arduino:')
		msg_from_arduino = read_arduino(ser)
		print(msg_from_arduino)

def write_arduino(serial_name, msg):
	serial_name.write(msg)

def read_arduino(serial_name):
	mesage_from_arduino = 'Arduino: '
	temp = serial_name.read()
	mesage_from_arduino += temp
	print(temp)

	return mesage_from_arduino

if __name__ == '__main__':
	main()
