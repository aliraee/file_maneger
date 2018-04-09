import socket
import threading

socketserver = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
socketserver.bind(('172.17.8.37',4444))
socketserver.listen(2)


#functions
def recive_server_from_client():
    buf = connection.recv(1024).decode('UTF-8')
    if len(buf) > 0:
        print(buf)
def send_to_client():
    mas = input().encode('UTF-8')
    connection.send(mas)




while True:
    connection,address = socketserver.accept()
    while True:
        t1 = threading.Thread( target = recive_server_from_client())
        t2 = threading.Thread( target = send_to_client())
        t1.start()
        t2.start()
        #t1.join()
        #t2.join()

        
        
