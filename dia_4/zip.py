nombres = ["Ama", "Hugo", "Valeria"]
edades = [65, 29, 42]
ciudades = ["Lima", "Madrid", "Mexico"]

# combinados = zip(nombres, edades) # Require inyectarlo en una lista
combinados = list(zip(nombres, edades, ciudades))

for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")
