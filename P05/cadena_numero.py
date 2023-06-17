import random

n = 20

def generar_numero_aleatorio():
    return random.randrange(0, 101)

def cantidad_numero_aleatorios(n):
    numeros_aleatorios = []
    for _ in range(n):
        m = generar_numero_aleatorio()
        numeros_aleatorios.append(m)

    return print(numeros_aleatorios)

cantidad_numero_aleatorios(n)


