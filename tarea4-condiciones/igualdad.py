'''
3. Escriba otro programa llamado igualdad.py que pida al usuario dos números y evalúe si el primer
valor ingresado es mayor, menor o igual al segundo valor ingresado.
'''
print ("Determinar si un numero es mayor, igual o menor")
num1 = float(input("Ingrese un primer número: "))
num2 = float(input("Ingrese el segundo número: "))
if num1 > num2:
    print("El primer número (", num1 ,") es mayor que el segundo (", num2 ,")")
elif num1 < num2:
    print("El primer número (", num1 ,") es menor que el segundo (", num2 ,")")
else:
    print("Ambos números son iguales.")