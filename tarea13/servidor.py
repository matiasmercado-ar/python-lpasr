'''
1. Cree dos archivos llamados servidor.py y cliente.py.
2. Importe el módulo correspondiente para trabajar con conexiones entre procesos.
3. Cree una conexión de tipo servidor en el archivo servidor.py que deberá indicar cada vez que
se establezca una conexión desde un cliente. El servidor deberá dejar la conexión abierta para
que cualquier cliente pueda conectar
4. Cree una conexión de tipo cliente en el archivo cliente.py. Este enviará un mensaje “Hola
Servidor!” al momento de realizar la conexión.
5. Replique el escenario utilizando una máquina virtual y trabajando con red LAN (la máquina
virtual debe estar en el mismo segmento de red que la máquina física, por lo que deberá
configurar el adaptador de la máquina virtual en modo bridge o puente). De esta forma su
Computador físico debe funcionar como servidor, mientras que la máquina cliente debe ser
cliente.
6. Realice capturas de pantalla de las conexiones logradas en ambos escenarios para adjuntar
'''

import socket

servidor_socket = socket.socket()
host = '192.168.100.14'
puerto = 65432
servidor_socket.bind((host, puerto))
servidor_socket.listen()

print(f"Servidor escuchando en {host}:{puerto}...")

while True:
    conexion, direccion = servidor_socket.accept()
    print(f"Conexión establecida desde {direccion}")
    mensaje = conexion.recv(1024)
    print(f"Mensaje recibido: {mensaje}")
    conexion.sendall(b"Mensaje recibido")
    conexion.close()
