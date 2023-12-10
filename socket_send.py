import socket
import threading

PACKET_SIZE = 1024


class Client:
    def __init__(self, ip, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((ip, port))
        print("Connected...")
        self.start()

    def send_msg(self, msg):
        message = str(msg).encode()
        msg_length = len(message)
        send_length = str(msg_length).encode()
        send_length += b' ' * (PACKET_SIZE - len(send_length))
        self.socket.send(send_length)
        self.socket.send(message)

    def recv_msg(self):
        msg_length = self.socket.recv(1024).strip()
        if msg_length:
            data = self.socket.recv(int(msg_length))
            return data
        return b''

    def start(self):
        pass
        # logic or override this function


class Server:
    def __init__(self, ip, port):
        self.address = (ip, port)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((ip, port))
        self.server_socket.listen()
        print("Started server at:", self.address)
        self.valid_ips = []
        self.client_list = {}

        while True:
            self.run()

    def accept_connections(self, connection, address):
        self.client_list[address] = connection
        self.talk(address)

    def talk(self, address):
        pass
        # logic or override this function

    def add_valid_ip(self, address):
        self.valid_ips.append(str(address))

    def send_msg(self, msg, conn):
        message = str(msg).encode()
        msg_length = len(message)
        send_length = str(msg_length).encode()
        send_length += b' ' * (PACKET_SIZE - len(send_length))
        conn.send(send_length)
        conn.send(message)

    def receive(self, conn):
        msg_length = conn.recv(1024).strip()
        if msg_length:
            data = conn.recv(int(msg_length))
            return data
        return b''

    def run(self):
        client_connected, client_address = self.server_socket.accept()
        thread = threading.Thread(target=self.accept_connections, args=(client_connected, client_address))
        thread.start()


if __name__ == "__main__":
    
    pass
