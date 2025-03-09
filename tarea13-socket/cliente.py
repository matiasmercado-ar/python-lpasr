import socket
import time

host = '192.168.100.14'
puerto = 65432

cliente_socket = socket.socket()
cliente_socket.connect((host, puerto))

cliente_socket.send(b'Hola Servidor!')

time.sleep(2)
respuesta = cliente_socket.recv(1024)
print(f"Respuesta del servidor: {respuesta}")

cliente_socket.close()
