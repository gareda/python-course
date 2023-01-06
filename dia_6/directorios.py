import os
from pathlib import Path

# ruta = os.getcwd()  # Ruta actual

"""
os.chdir("C:\\Users\\Usuario\\Desktop\\Python\\Alternativo")  # Cambia la ruta
archivo = open("otro_archivo.txt")
print(archivo.read())
"""

# os.makedirs("C:\\Users\\Usuario\\Desktop\\Python\\Alternativo\\otra")  # Crea un directorio o archivo

"""
ruta = "C:\\Users\\Usuario\\Desktop\\Python\\Dia 6\\prueba.txt"
elemento = os.path.basename(ruta)  # Archivo
print(elemento)
elemento = os.path.dirname(ruta)  # Ruta
print(elemento)
elemento = os.path.split(ruta)  # Ambos en una tupla
print(elemento)
"""

# os.rmdir("C:\\Users\\Usuario\\Desktop\\Python\\Alternativo\\otra")  # Borrar directorio

"""
otro_archivo = open("C:\\Users\\Usuario\\Desktop\\Python\\Alternativo\\otro_archivo.txt")
print(otro_archivo.read())
"""

carpeta = Path("C:/Users/Usuario/Desktop/Python/Alternativo")
archivo = carpeta / "otro_archivo.txt"

mi_archivo = open(archivo)
print(mi_archivo.read())
