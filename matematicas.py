"""
Modulo: matematicas.py 
Descripcion: Contiene funciones matematicas basicas
Autor: Grupo de programacion 3 
"""
def suma(a, b):
    """Retorna la suma de dos numeros"""
    return a + b

def resta(a, b):
    """Retorna la resta de dos numeros"""
    return a - b

def multiplicacion(a, b):
    """Retorna la multiplicacion de dos numeros"""
    return a * b

def division(a, b):
    """Retorna la division de dos numeros"""
    if b != 0:
        return a / b
    else:
        return "No se puede dividir entre cero"

def potencia(a, b): 
    """Retorna la potencia de dos numeros"""
    return a ** b

def modulo(a, b):
    """Retorna el modulo de dos numeros"""
    return a % b 
