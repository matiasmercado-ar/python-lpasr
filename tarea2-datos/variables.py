""""
1. Usando la función de impresión, imprima su nombre completo
2. Imprima su nombre completo, pero esta vez usando una línea por cada parte
3. Guarde su nombre completo en la variable NombreCompleto
4. Utilice una variable asignada como entrada por el usuario para almacenar su e-mail
5. ¿Cuántos caracteres hay en la variable NombreCompleto?
6. Utilizando la variable NombreCompleto, imprima solo su primer nombre, usando la
impresión de rango de caracteres de una variable
7. Imprima el mes de su cumpleaños TODO EN MAYÚSCULAS
8. Imprima su nombre con minúscula, excepto la letra inicial y su apellido TODO CON
MAYÚSCULA
"""

#1
print ('Matías Mercado')
#2
print ('Matías \nMercado')
#3
NombreCompleto = 'Matías Mercado'
#4
email=input("Ingrese su email: ")
print(email)
#5
print (len(NombreCompleto))
#6
print('Nombre: ',NombreCompleto[0:6])
#7
mesCumpleanios='septiembre'
print('Mes de cumpleaños es: ',mesCumpleanios.upper())
#8
nombre, apellido = NombreCompleto.split()

resultado = f"{nombre.capitalize()} {apellido.upper()}"
print(resultado)



