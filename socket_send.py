import socket
import threading

PACKET_SIZE = 1024


class Client:
	def __init__(self,ip,port):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.connect((ip,port))
		print("Connected...")
		self.start()
	def send_msg(self,msg):
		message = str(msg).encode()
		msg_length = len(message)
		send_length = str(msg_length).encode()
		send_length += b' ' * (PACKET_SIZE - len(send_length))
		self.socket.send(send_length)
		self.socket.send(message) 
		

	def recv_msg(self):
		msg_length = self.socket.recv(1024)
		data = self.socket.recv(int(msg_length))
		return data
	
	def start(self):
		pass
		#logic or override this function 




class Sever:
	def __init__(self,ip,port):
		self.address = [ip,port]
		self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server_socket.bind((ip,port))
		self.server_socket.listen()
		print("Started server at :",self.adress)
		self.valid_ips = []
		self.client_list = {}
		
		while True:
			self.run()

	def accept_connections(self,connection,address):
		self.client_list[address] = connection
		self.talk(adress)
		
		
	def talk(self,address):
		if address in valid_ips:
			pass
		   #logic or override this function 
		
	def add_valid_ip(self,address):
		self.valid_ips.append(str(adress))

	def send_msg(self,msg,conn):
		message = str(msg).encode()
		msg_length = len(message)
		send_length = str(msg_length).encode()
		send_length += b' ' * (PACKET_SIZE - len(send_length))
		conn.send(send_length)
		conn.send(message)    

	
	def recieve(self,conn):
		msg_length = conn.recv(1024)
		data = conn1.recv(int(msg_length))
		return data

		
	
	def run(self):
		(clientConnected, clientAddress) = self.server_socket.accept()
		thread  = threading.Thread(target = self.accept_connections , args = (clientConnected,clientAddress))
		thread.start()
		


if __name__ == "__main__":
	pass