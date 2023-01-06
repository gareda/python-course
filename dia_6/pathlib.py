from pathlib import Path, PureWindowsPath

carpeta = Path("C:/Users/Usuario/Desktop/Python/Dia 6/pruebas.txt")

# print(carpeta.read_text())  # Leer sin abrir
# print(carpeta.name)  # Nombre de archivo
# print(carpeta.suffix)  # Extension
# print(carpeta.stem)  # Nombre de archivo sin extension

"""
if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("Genial, existe")
"""

ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)
