'''
1. Cree un archivo llamado operaciones.py.
2. En este archivo cree una clase llamada Operaciones, que será una clase principal.
3. Esta clase tendrá un constructor que definirá dos atributos llamados num1 y num2
4. Luego cree 4 clases que hereden de la clase Operaciones. Estas subclases se llamarán Suma,
Resta, Producto y Cociente.
5. Defina en cada subclase un método que realice la operación correspondiente al nombre de
la subclase (método sumar() para la subclase Suma, restar() para la subclase Resta, etc).
Cada método retornará la operación de los atributos correspondiente con su nombre. Tenga
en cuenta para la operación cociente considerar si el primer número es 0 (no se puede dividir
por cero).
6. Para corroborar el correcto funcionamiento, cree un objeto de cada subclase e imprima para
cada uno de ellos el método correspondiente a la operación.

'''

class Operaciones:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

# Subclases
class Suma(Operaciones):
    def sumar(self):
        return self.num1 + self.num2

class Resta(Operaciones):
    def restar(self):
        return self.num1 - self.num2

class Producto(Operaciones):
    def multiplicar(self):
        return self.num1 * self.num2

class Cociente(Operaciones):
    def dividir(self):
        if self.num2 == 0:
            return "Error: No es posible la división por cero."
        return self.num1 / self.num2

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

suma = Suma(num1, num2)
resta = Resta(num1, num2)
producto = Producto(num1, num2)
cociente = Cociente(num1, num2)

print(f"Suma de {num1} y {num2} es: {suma.sumar()}")
print(f"Resta de {num1} y {num2} es: {resta.restar()}")
print(f"Multiplicacion de {num1} y {num2} es: {producto.multiplicar()}")
print(f"División dee {num1} en {num2} es: {cociente.dividir()}")
