import math

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

# De:
def dividir(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida")
    return a / b

# Para:
def dividir(a, b, arredondar):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida")
    resultado = a / b

def raiz_quadrada(n):
    if n < 0:
        raise ValueError("Raiz de número negativo não é definida nos reais")
    return math.sqrt(n)