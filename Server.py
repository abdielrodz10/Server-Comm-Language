# Remote server class declaration
import sys
import socket


class Server:
    def __init__(self, ip='', port='4444'):
        self.skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.ip = ip
        self.port = port

        self.connected_clients = list()
        self.limit_simultaneous = 2

        try:
            self.skt.bind((ip, int(port)))
        except socket.error as msg:
            print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
            sys.exit()

        print('Socket bind complete')

        self.skt.listen(10)
        print('Socket listening')

        print('Server Listening on {}:{}'.format(self.ip, self.port))

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



