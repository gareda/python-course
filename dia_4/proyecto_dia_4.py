# Preguntar nombre de usuario
# He pensado un numero entre el 1 y el 100, tienes 8 intentos para averiguarlo
# Si el numero es menos a 1 o mayor a 100 -> el numero no esta permitido
# Si el numero es menor al que ha pensado el programa -> No es correcto, el numero es menos al escogido
# Si el numero es mayor al que ha pensado el programa -> No es correcto, el numero es maoyr al escogido
# Si el numero es correcto -> Es correcto y te ha llevado X intentos

from random import randint

nombre = input("Bienvenido al juego \"Adivina que número he pensado\".\nDinos cual es tu nombre: ")
print(f"Buenas {nombre}, gracias por jugar.\n")
print("Estoy pensando en un número entre el 1 y el 100.\nTienes tienes 8 intentos para averiguarlo.")

numero = randint(1, 100)
intentos = 0
repetir = "y"

while repetir == "y":
    while intentos < 8:
        intentos += 1
        respuesta = int(input("¿En que número estoy pensando?: "))

        if respuesta == numero and 0 < respuesta < 101:
            print("\nEnhorabuena, has acertado en que numero estaba pensando.")
            print(f"Lo has conseguido en {intentos} intentos.")
            break
        elif respuesta < numero and 0 < respuesta < 101:
            print(f"\nEl numero en el que estoy pensando es mayor a {respuesta}.\nVuelve a intentarlo.")
        elif respuesta > numero and 0 < respuesta < 101:
            print(f"\nEl numero en el que estoy pensando es menor a {respuesta}.\nVuelve a intentarlo.")
        else:
            print("\nNo es un número valido.\nLa respuesta esta entre los números 1 al 100")

    if intentos > 8:
        print("\nSe acabaron los intentos.")

    repetir = input("\n¿Quieres jugar otra vez? y/n : ")
    if repetir == "y":
        intentos = 1

print("Gracias por jugar :).")
