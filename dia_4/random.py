# from random import randint
from random import *

"""
# aleatorio = randint(1, 50)
# aleatorio = round(uniform(1, 50), 1)
aleatorio = random()
print(aleatorio)
"""

# colores = ["azul", "rojo", "verde", "amarillo"]
# aleatorio = choice(colores)
# print(aleatorio)

numeros = list(range(5, 50, 5))
shuffle(numeros)
print(numeros)