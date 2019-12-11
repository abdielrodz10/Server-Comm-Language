# Remote server class declaration
import socket


class Server:
    def __init__(self, ip='', port='4444'):
        self.skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.ip = ip
        self.port = port

        self.connected_clients = list()
        self.limit_simultaneous = 2

        self.skt.bind((ip, int(port)))

    def get_ip(self):
        return self.ip

    def get_port(self):
        return self.port

    def get_connected_clients(self):
        return self.connected_clients

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



