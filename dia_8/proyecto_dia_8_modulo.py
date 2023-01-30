def mensaje_turno(funcion):
    print("\n" + "*" * 23)
    print("Su número es: ")
    if funcion == "P":
        print(next(p))
    elif funcion == "F":
        print(next(f))
    else:
        print(next(c))
    print("Aguarde y sera atendido")
    print("*" * 23 + "\n")


def turno_perfumeria():
    for turno in range(1, 100):
        yield f"P-{turno}"


def turno_farmacia():
    for turno in range(1, 100):
        yield f"F-{turno}"


def turno_cosmetica():
    for turno in range(1, 100):
        yield f"C-{turno}"


p = turno_perfumeria()
f = turno_farmacia()
c = turno_cosmetica()
