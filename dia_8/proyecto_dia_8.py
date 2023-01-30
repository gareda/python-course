import proyecto_dia_8_modulo


def preguntar():
    print("Bienvenido a Farmacia Python")

    while True:
        print("[P] - Perfumería\n[F] - Farmacia\n[C] - Cosmetica")
        try:
            mi_negocio = input("Elija su negocio: ").upper()
            ["P", "F", "C"].index(mi_negocio)
        except ValueError:
            print("Esa no es una opción válida")
        else:
            break

    proyecto_dia_8_modulo.mensaje_turno(mi_negocio)


def inicio():
    while True:
        preguntar()
        try:
            otro_turno = input("¿Quieres sacar otro turno? [S] [N]").upper()
            ["S", "N"].index(otro_turno)
        except ValueError:
            print("Esa no es una opción válida")
        else:
            if otro_turno == "N":
                print("Gracias por su visita")
                break


inicio()