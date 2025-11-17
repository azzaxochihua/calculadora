# Dev 1 - Funciones matemáticas básicas

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # Manejar división entre cero
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b
