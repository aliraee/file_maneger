import sys
import socket
import select

class server:
    def __init__(self):
        self.host = 'localhost'
        self.buffer = 4096
        self.port = 8585
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []
        self.start()

    def start(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(90)
        print("server started on port", str(self.port))
        self.render()

    def render(self):
        while True:
            client, addr = self.socket.accept()
            print("Got a connection from", str(addr))
            self.clients.append(client)
            if len(self.clients) == 2:
                break
        while True:
            data = self.clients[0].recv(self.buffer).decode('ascii')
            data = self.clients[1].recv(self.buffer).decode('ascii')
            if data[0] == '1':
                data = data[1:]
                self.clients[0].sendall(data.encode('ascii'))
            elif data[0] == '2':
                data = data[1:]
                self.clients[1].sendall(data.encode('ascii'))
            pass

    def send_to_client_1(self, data):
        self.clients[0].sendall(data.encode('ascii'))

    def send_to_client_2(self, data):
        self.clients[1].sendall(data.encode('ascii'))

s = server()