'''
2. Desarrolle un programa llamado paridad.py que pida un número por teclado al usuario y
determine si ese número es par o impar
'''
print("Determinar si el numero es par o impar")
numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print ("El numero es par")
else:
    print ("El numero es inpar")
