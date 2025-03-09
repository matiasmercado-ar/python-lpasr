import socket

host = '192.168.100.14'
puerto = 65432

cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_socket.connect((host, puerto))

mensaje = "Hola Servidor!"
cliente_socket.sendall(mensaje.encode())

respuesta = cliente_socket.recv(1024).decode()
print(f"Respuesta del servidor: {respuesta}")

cliente_socket.close()
