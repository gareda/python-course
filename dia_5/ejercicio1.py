def devolver_distintos(int1, int2, int3):
    suma = int1 + int2 + int3
    numeros = [int1, int2, int3]
    numeros.sort()

    if suma > 15:
        return numeros[2]  # Numero mayor
    elif suma < 10:
        return numeros[0]  # Numero menor
    else:
        return numeros[1]  # Numero del medio


print(devolver_distintos(3, 5, 4))
