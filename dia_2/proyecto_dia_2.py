nombre = input("¿Cual es tu nombre?: ")
ventas = float(input("¿Cuanto has vendido este mes?: "))

ganancias = round(ventas * 13 / 100, 2)

print(f"Ok {nombre}. Este mes ganaste ${ganancias}")