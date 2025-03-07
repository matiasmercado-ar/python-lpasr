def suma(a, b):
    resultado = a + b
    print(f"{a} + {b} = {resultado}")
    return resultado

def resta(a, b):
    resultado = a - b
    print(f"{a} - {b} = {resultado}")
    return resultado

def multiplicacion(a, b):
    resultado = a * b
    print(f"{a} * {b} = {resultado}")
    return resultado

def division(a, b):
    if b == 0:
        print("Error: No se puede dividir por cero.")
        return None
    resultado = a / b
    print(f"{a} / {b} = {round(resultado,3)}")
    return resultado

# Main
def main():
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    
    suma(a, b)
    resta(a, b)
    multiplicacion(a, b)
    division(a, b)

if __name__ == "__main__":
    main()