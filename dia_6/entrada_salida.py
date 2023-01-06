mi_archivo = open("prueba.txt")

# print(mi_archivo.read())

"""
print(mi_archivo.readline())  # Solo una linea
print(mi_archivo.readline())
print(mi_archivo.readline())
"""

# for linea in mi_archivo:
#     print("Aqui dice: " + linea)

todas = mi_archivo.readlines()  # RECOMENDACION: No usar con archivos grances, puede sobre cargar el siestema
print(todas)
todas = todas.pop()
print(todas)

mi_archivo.close()
