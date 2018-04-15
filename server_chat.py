import socket
import threading
class server:
    def __init__(self, to):
        self.to = to
        self.msg = ''
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(('127.0.0.1', 9909))
        self.s.listen(2)
        self.client, self.ip = self.s.accept()
#functions
    def recive(self):
        buf = self.client.recv(1024).decode('UTF-8')
        if len(buf) > 0:
            self.msg+=buf
        return self.msg
    def send(self,msg):
        self.client.sendall(msg.encode('UTF-8'))
