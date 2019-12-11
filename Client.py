# Local client class declaration
import socket


class Client:
    def __init__(self, ip='localhost', port='4444'):
        self.skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = ip
        self.port = port

        self.connect(ip, int(port))

    def get_ip(self):
        return self.ip

    def get_port(self):
        return self.port

    def connect(self, ip, port):
        try:
            self.skt.connect((ip, int(port)))
            print("Client connected successfully!")
        except:
            print("Error establishing connection to server...")

    def disconnect(self):
        self.skt.close()

    # def send_message(self, payload):
    #     try:
    #         self.skt.send(payload)
    #         print("Message sent!")
    #     except:
    #         print("Could not send message...")

