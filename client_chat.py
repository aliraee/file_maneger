import socket
import threading

clinet = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
clinet.connect(('172.17.8.37',4444))

#functions
def send_client_to_server():
    clinet.send(input().encode('UTF-8'))
def recive_client_from_server():
    mas1 = clinet.recv(1024).decode('UTF_8')
    if len(mas1) != 0:
        print(mas1)

while True:
    t1 = threading.Thread( target = send_client_to_server())
    t2 = threading.Thread( target = recive_client_from_server())
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    
