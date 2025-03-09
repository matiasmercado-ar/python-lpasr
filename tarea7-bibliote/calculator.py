'''
1. Cree un módulo en el que se definan las cuatro operaciones aritméticas principales (definir
las funciones). Este archivo deberá llamarlo calculadora.py.
2. Luego importe la biblioteca en un archivo de implementación llamado implementación.py
que utilizará para importar el módulo creado en el punto anterior y realizar operaciones.
Realice al menos una suma, una resta, una multiplicación y una división en este último
archivo. Los parámetros puede tomarlos de la entrada del usuario o podrá utilizar valores
estáticos.
'''

def suma(a, b):
    resultado = a + b
    return resultado

def resta(a, b):
    resultado = a - b
    return resultado

def multiplicacion(a, b):
    resultado = a * b
    return resultado

def division(a, b):
    if b == 0:
        print("Error: No se puede dividir por cero.")
        return None
    resultado = a / b
    return resultado