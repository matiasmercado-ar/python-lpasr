'''
1 - Cree un programa llamado valor.py que permita ingresar por el usuario un valor numérico y que
al ejecutarse muestre si ese número es positivo o negativo.

'''
print("Determinar si un numero es positivo negativo o cero")
numero = float(input("Ingrese un numero: "))
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")