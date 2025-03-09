'''
1. Cree un archivo llamado usuarios.py.
2. Importe el módulo correspondiente para trabajar con ficheros
3. Cree el archivo de apertura de un fichero llamado fichero.csv, que contendrá datos de
usuarios.
4. Los datos que contendrá el archivo se obtendrán de la interacción con el usuario. El programa
debe pedir a los usuarios el nombre, el apellido, la edad y la profesión actual que se irán
agregando al archivo en cada ejecución. Todos esos datos deberán concatenarse utilizando
el siguiente esquema:
Nombre|Apellido|Edad|Profesión
De esta forma se expone un ejemplo completado por Alfio y José a modo de demostración
de cómo debe verse el archivo luego de dos ejecuciones (debe agregar el | tras cada dato).
Alfio|Canal|32|Docente
José|Gagliano|43|Comerciante
5. Escriba los datos proporcionados por el usuario.
6. Cierre el archivo y vuélvalo a abrir en modo lectura para leer el contenido del archivo en cada
ejecución y mostrar en pantalla el resultado final del archivo
'''

import io

def obtener_datos_usuario():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = input("Edad: ")
    profesion = input("Profesión: ")
    return f"{nombre}|{apellido}|{edad}|{profesion}\n"

datos_usuario = obtener_datos_usuario()

archivo = open('fichero.csv', 'w')

archivo.write(datos_usuario)

archivo.close()

archivo = open('fichero.csv', 'r')

lectura = archivo.read()
print(lectura)

archivo.close()


