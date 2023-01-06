# lista = ["a", "b", "c"]
#
# for indice, item in enumerate(lista):
#     print(indice, item)

"""
for indice, item in enumerate(range(50, 55)):
    print(indice, item)
"""

lista = ["a", "b", "c"]

mi_tuples = list(enumerate(lista))
print(mi_tuples[1][0])