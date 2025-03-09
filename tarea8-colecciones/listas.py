'''
1. Cree un archivo llamado listas.py.
2. En el archivo listas.py cree una lista de elementos conformado por componentes de hardware
de una PC de escritorio (al menos 5 elementos). Cree una estructura iterativa que imprima en
pantalla cada uno de los elementos. Luego cree una función llamada imprimir que tome una
entrada del usuario relacionada al índice del elemento a mostrar (recuerde convertir la
entrada del usuario en entero con int()) y luego haga el llamado de la función que mostrará
en pantalla el elemento correspondiente al índice expresado por el usuario.

'''

hardware_pc = ["Procesador", "Memoria RAM", "Placa Madre", "SSD", "Fuente", "Placa de Video"]

print("Componentes de hardware de una PC:")
for componente in hardware_pc:
    print(componente)

def imprimir():
    indice = int(input("Ingrese el índice del elemento que desea ver: "))
    if 0 <= indice < len(hardware_pc):
        print(f"El componente en el índice {indice} es: {hardware_pc[indice]}")
    else:
        print("Índice fuera de rango. Debe ser un número entre 0 y 5.")

imprimir()
