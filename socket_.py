import socket

host = '192.168.122.238'
port = 15001
username = 'vm01'
password = '123456'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	server_address = (host, port)
	sock.connect(server_address)
	sock.sendall("stop c:\\soft\\bin\\SCADAMake.exe")
finally:
	sock.close()