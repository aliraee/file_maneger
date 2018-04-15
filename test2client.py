import socket

class client:
    def __init__(self, host, port):
        self.name = '2'
        self.host = host
        self.port = port
        self.buffer = 4096
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.start()

    def start(self):
        self.socket.connect((self.host, self.port))
        print("client "+self.name+" connected")
        self.render()

    def render(self):
        self.send_chat("hi from 2")
        while True:
            pass

    def send_chat(self, msg):
        msg = "1"+msg
        data = msg.encode('ascii')
        self.socket.sendall(data)

c = client('localhost', 8585)