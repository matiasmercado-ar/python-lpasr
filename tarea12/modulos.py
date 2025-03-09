'''
1. Cree un archivo llamado modulos.py.
2. Importe los módulos correspondientes para trabajar con métodos que interactúan con el
sistema operativo, variables e información de la plataforma y comandos del sistema.
3. Muévase a un directorio diferente aplicando un método.
4. Liste este directorio.
5. Cree un archivo en ese directorio llamado Alumno.txt que contenga su nombre y Luego
renombre el mismo a Alumno.csv.
6. Mueva de lugar el archivo a otro directorio con un método y elimine el directorio desde donde
lo movió.
7. Muestre la versión del intérprete que ejecuta su equipo.
8. Muestre la plataforma donde está programando
9. Cree una estructura en la que se le pida al usuario que ingrese un comando seleccionado de
una lista de comandos de sistemas Linux. Según el comando seleccionado el intérprete
deberá responder ejecutando ese comando en el sistema operativo. (No puede utilizar para
este ejercicio los comandos ls, df, du ni htop).
'''

import os
import sys
import subprocess
import io

os.chdir("/home/matiasm/Desktop/test")
print(os.listdir())

archivo = open('Alumno.txt', 'w')
archivo.write("Matías Mercado")

os.rename("Alumno.txt", "Alumno.csv")

os.rename("Alumno.csv", "/home/matiasm/Desktop/Alumno.csv")

os.rmdir("/home/matiasm/Desktop/test")

archivo.close()

print(sys.version)

print(sys.platform)

comandos = {
    1: "uname -a",
    2: "ps -fax",
    3: "w"
}

print("Selecciona un comando:")
for instruccion, valor in comandos.items():
    print(f"{instruccion}: {valor}")

seleccion = int(input())

comando = comandos.get(seleccion)

if comando:
    subprocess.run(comando, shell=True)
else:
    print("Comando no válido.")
