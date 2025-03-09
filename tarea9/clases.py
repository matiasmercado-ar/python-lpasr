'''
1. Cree un archivo llamado clases.py.
2. En este archivo cree una clase llamada Suma.
3. Esta clase tendrá un constructor que definirá dos atributos llamados num1 y num2
4. Cree un método por el cual se retorne la suma de ambos atributos, como si fuera una
calculadora simple de sumas de dos números.
5. Para verificar el funcionamiento, instancie un objeto llamado suma que tome como valores
de los atributos del constructor a través de lo que ingrese el usuario por teclado (con
int(input()) para convertir el dato ingresado en un entero).
6. Luego imprima por pantalla el llamado al método creado en el punto 4 que deberá retornar
la suma de los atributos del objeto.
'''


class Suma:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calcular_suma(self):
        return self.num1 + self.num2

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

suma = Suma(num1, num2)


print(f"La suma de {num1} y {num2} es: {suma.calcular_suma()}")
