# 1. Veces que aparece cada letra
# 2. Cuantas palabras hay en total
# 3. Primera y última letra
# 4. Palabras en orden inverso
# 5. ¿aparece la palabra python?

texto = input("Hola usuario, introduce el texto que desees: ", input)

# Solución 1
letra1 = input("Cual es la primera letra: ").lower()
letra2 = input("Cual es la segunda letra: ").lower()
letra3 = input("Cual es la tercera letra: ").lower()

letra1_count = texto.lower().count(letra1)
letra2_count = texto.lower().count(letra2)
letra3_count = texto.lower().count(letra3)

print(
    f"\nLa letra {letra1} aparece {letra1_count} veces, \n"
    f"La letra {letra2} aparece {letra2_count} veces, \n"
    f"La letra {letra3} aparece {letra3_count} veces."
)

# Solución 2
palabras = len(texto.split())
print(f"El texto tiene {palabras} palabras.")

# Solución 3
print(f"\n La primera letra del texto es {texto[0]} y la ultima es {texto[-1]}")

# Solución 4
palabras = texto.split()
palabras.reverse()
texto_inverso = " ".join(palabras)
print(texto_inverso)

# Solución 5
python = texto.lower().find("python")
existe_python = python >= 0
solucion = {True: "Sí", False: "No"}
print(F"\n ¿Esta la palabra python en el texto?: {solucion[existe_python]}")
