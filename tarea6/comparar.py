'''
2 - Cree otro programa llamado comparar.py para determinar el número más grande y el más chico
a partir de una cantidad previamente consultada de números ingresada por el usuario. El usuario
ingresa el número que representa la cantidad de números a ingresar y luego ingresa todos los valores
consecutivos hasta terminar. Luego el programa debe mostrar en dos líneas cuál es el valor más
grande y cuál el más chico.

'''

cantidad = int(input("Ingrese la cantidad de números a comparar: "))

if cantidad <= 0:
    print("Debe ingresar al menos un número.")
else:
    numeros = []
    for i in range(cantidad):
        num = int(input(f"Ingrese el número {i+1}: "))
        numeros.append(num)
    
    print("Los números ingresados son: ")
    for num in numeros:
        print(num)

    print(f"El número más grande es: {max(numeros)}")
    print(f"El número más chico es: {min(numeros)}")
