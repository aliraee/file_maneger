import socket

clinet = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
clinet.connect(('localhost',4444))
while True:
    clinet.send(input().encode('UTF-8'))
