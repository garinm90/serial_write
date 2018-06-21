#!/usr/bin/env python          
import time
import serial

carriage = "\n"
ser = serial.Serial(port='/dev/ttyUSB0',baudrate = 115200)

while 1:
	data = 'p' + carriage
	print 'Sending', data
	time.sleep(5)
	ser.write(data)
	print 'Payload Sent'
	exit()
