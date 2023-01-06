# 1 Importar el metodo choice
# 2 Crear funciones: pedir letra, validar letra, chequear letra, ver si gano
# El jugador tiene 6 vidas

from random import choice


def elegir_palabra():
    palabras = ["camaleon", "camello", "ciempies", "leon", "avispa", "tiguron"]
    return choice(palabras)


def ocultar_palabra(palabra):
    oculto = ""
    contador = len(palabra)

    while contador != 0:
        oculto += "_"
        contador -= 1

    return oculto


def pedir_letra():
    letra = input("Introduce una letra: ")
    return letra


def validar_letra(letra):
    if len(letra) > 1:
        print("\nUn texto uno es un valor valido, debes introducir una unica letra.")
        return False
    elif len(letra) < 1:
        print("\nDebes introducir por lo menos una letra.")
        return False
    elif not letra.isalpha():
        print("\nUn número no es un valor valido, debes introducir una unica letra.")
        return False
    else:
        return True


def comprobar_letra(letra, palabra, oculto):
    letras = " ".join(oculto).split(" ")

    if letra in palabra:
        contador = 0

        for caracter in palabra:

            if letra == caracter:
                letras[contador] = letra

            contador += 1

        return "".join(letras), True

    else:
        return "".join(letras), False


def contador_vidas(vida, restar):
    if not restar:
        vida -= 1

        if vida == 0:
            vivo = False

    return vida


def partida(vidas, palabra, oculto):
    victoria = False
    derrota = False

    while oculto != palabra:
        valido = False

        while not valido:
            letra = pedir_letra()
            valido = validar_letra(letra)

        oculto, restar_vida = comprobar_letra(letra, palabra, oculto)
        vidas = contador_vidas(vidas, restar_vida)

        if vidas > 0:
            if oculto == palabra:
                return True
            else:
                print(f"{oculto} (Intentos restantes: {vidas})")
        else:
            return False


def juego():
    repetir = "y"

    while repetir == "y":
        vidas = 6
        palabra_escogida = elegir_palabra()
        palabra_oculta = ocultar_palabra(palabra_escogida)

        if partida(vidas, palabra_escogida, palabra_oculta):
            print("Enhorabuena, has ganado.")
        else:
            print("Lo siendo, has perdido.")

        repetir = input("\n¿Quieres jugar otra vez? y/n : ")


juego()
