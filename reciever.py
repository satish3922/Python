#!/usr/bin/python

import socket

#s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s=socket.socket()

s.bind(("",1999))

s.listen(5)

while True:
	clisocket,cliaddr=s.accept()
	print  clisocket.recv(100)


s.close()
