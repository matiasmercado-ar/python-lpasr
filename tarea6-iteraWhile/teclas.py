'''
1 - Cree un programa llamado teclas.py que imprima en pantalla los caracteres que el usuario va
colocando hasta que se presione la tecla enter sin ingresar valor.
'''

print("Introduce caracteres. Presiona Enter sing nada para finalizar.")

while True:
    userInput = input()
    if userInput == "":
        print("\nFin del script")
        break


