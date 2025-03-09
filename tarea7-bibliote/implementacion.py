'''
1. Cree un módulo en el que se definan las cuatro operaciones aritméticas principales (definir
las funciones). Este archivo deberá llamarlo calculadora.py.
2. Luego importe la biblioteca en un archivo de implementación llamado implementación.py
que utilizará para importar el módulo creado en el punto anterior y realizar operaciones.
Realice al menos una suma, una resta, una multiplicación y una división en este último
archivo. Los parámetros puede tomarlos de la entrada del usuario o podrá utilizar valores
estáticos.
'''

import calculator

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

print(f"La suma de ambos numeros es: ",calculator.suma(a,b))
print(f"La resta de ambos numeros es: ",calculator.resta(a,b))
print(f"La multiplicacion de ambos numeros es: ",calculator.multiplicacion(a,b))
print(f"La division de ambos numeros es: ",calculator.division(a,b))



