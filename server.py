import socket

socketserver = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
socketserver.bind(('localhost',4444))
socketserver.listen(2)

while True:
    connection,address = socketserver.accept()
    while True:
        buf = connection.recv(1024).decode()
        if len(buf) > 0:
            print(buf)
        
        
