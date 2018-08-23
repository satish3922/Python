import socket,time

# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s=socket.socket()

s.connect(("192.168.10.87",1999))

while True:
	s.send("hiiiiiiiiiiiiiiiiiiiiiiiiiiiiii....")
	time.sleep(2)
s.close()
