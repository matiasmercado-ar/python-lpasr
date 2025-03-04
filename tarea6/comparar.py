'''
2 - Cree otro programa llamado comparar.py para determinar el número más grande y el más chico
a partir de una cantidad previamente consultada de números ingresada por el usuario. El usuario
ingresa el número que representa la cantidad de números a ingresar y luego ingresa todos los valores
consecutivos hasta terminar. Luego el programa debe mostrar en dos líneas cuál es el valor más
grande y cuál el más chico.

'''


cantidad = int(input("Ingrese la cantidad de números a comparar: "))

numeros = []
i = 0

while True:
    if i >= cantidad:
        break

    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)
    i += 1

print("Los números ingresados son:")

j = 0

while True:
    if j >= cantidad:
        break
    print(numeros[j])
    j += 1

print(f"El número más grande es: {max(numeros)}")
print(f"El número más chico es: {min(numeros)}")


