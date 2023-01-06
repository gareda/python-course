def transformar(palabra):
    letras = set()

    for letra in palabra:
        letras.add(letra)

    letras = list(letras)
    letras.sort()

    return letras


print(transformar("entretenido"))
