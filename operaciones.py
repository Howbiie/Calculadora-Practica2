def suma(a,b):
    return a + b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    if b == 0:
        return "No division entre 0"
    return a/b

def potencia(base, exponente):
    return base ** exponente

def modulo(a, b):
    if b == 0:
        return "No se puede calcular modulo entre 0"
    return a % b

def raiz_cuadrada(numero):
    if numero < 0:
        return "No se permite raiz cuadrada de negativos"
    return numero ** 0.5

def porcentaje(cantidad, porciento):
    return cantidad * porciento / 100

def valor_absoluto(numero):
    return abs(numero)

def factorial(numero):
    if not isinstance(numero, int) or numero < 0:
        return "El factorial requiere un entero no negativo"
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado
