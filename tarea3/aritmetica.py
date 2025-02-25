"""
1 - Crear un programa sencillo llamado aritmética.py que permita ingresar por el usuario dos valores
numéricos y que calcule utilizando operadores aritméticos las cuentas correspondientes, y muestre
como salida lo siguiente:
La suma de ambos números es: resultado
La resta de ambos números es: resultado
El producto de ambos números es: resultado
La división de ambos números es: resultado
"""

# Solicitar al usuario dos valores numéricos
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Realizar operaciones aritméticas
suma = num1 + num2
resta = num1 - num2
producto = num1 * num2
division = num1 / num2 if num2 != 0 else "Indefinida (división por cero)"

# Mostrar los resultados
print(f"La suma de ambos números es: {suma}")
print(f"La resta de ambos números es: {resta}")
print(f"El producto de ambos números es: {producto}")
print(f"La división de ambos números es: {division}")
