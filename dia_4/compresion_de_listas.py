palabra = "python"

# lista = []

# for letra in palabra:
#     lista.append(letra)

"""
lista = [letra for letra in palabra]
"""

"""
# lista = [int(n / 2) for n in range(0, 20, 2)]
# lista = [n for n in range(0, 20, 2) if n * 2 > 10]
lista = [n if n * 2 > 10 else "no" for n in range(0, 20, 2)]

print(lista)
"""

pies = [10, 20, 30, 40, 50]
metros = [p * 3.281 for p in pies]
print(metros)
