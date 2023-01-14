from os import system
from random import randint


def programa():
    opciones = {
        1: "Mostrar datos de usuario",
        2: "Depositar dinero en la cuenta",
        3: "Retirar dinero de la cuenta",
        4: "Desconectar"
    }

    print("Bienvenido a la banca Corneone.")

    usuario = crear_cliente()

    while True:
        opcion = menu(opciones)

        match opcion:
            case 1:
                usuario.datos_cliente()
                input("\n(Pulsa cualquier intro para volver a manu inicial)")
            case 2:
                usuario.ingresar_dinero()
                input("\n(Pulsa cualquier intro para volver a manu inicial)")
            case 3:
                usuario.retirar_dinero()
                input("\n(Pulsa cualquier intro para volver a manu inicial)")
            case 4:
                break

        system("cls")


def crear_cliente():
    nombre = input("Cual es tu nombre: ")
    apellido = input("Cual es tu apellido: ")
    usuario = Cliente(nombre, apellido)
    return usuario


def menu(opciones):
    validacion = False

    while not validacion:
        imprimir_menu(opciones)
        opcion = solicitar_opcion("acción")
        validacion = validar_opcion(opciones, opcion)

    return int(opcion)


def imprimir_menu(opciones):
    for posicion, opcion in opciones.items():
        print(f"[{posicion}] - {opcion}")


def solicitar_opcion(tipo):
    return input(f"¿Que {tipo} quieres escoger?: ")


def validar_opcion(opciones, opcion):
    if not opcion.isalpha():
        if len(opcion) == 1:
            if int(opcion) in opciones:
                return True

    print("Debes introducion una opcion valida.")
    return False


class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, saldo=0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = str(randint(0, 100000000)).zfill(8)
        self.saldo = saldo

    def datos_cliente(self):
        print(f"Numero de cuenta: {self.numero_cuenta}")
        print(f"Usuario: {self.nombre} {self.apellido}")
        print(f"Saldo actual: {self.saldo}")
        return

    def ingresar_dinero(self):
        ingresar = float(input("¿Cuanto dinero deseas ingresar?: "))
        self.saldo += float(ingresar)
        print(f"Tu saldo es {self.saldo}")

    def retirar_dinero(self):
        repetir = True

        while repetir:
            retirar = float(input("¿Cuanto dinero deseas retirar?: "))

            if not retirar > self.saldo:
                self.saldo -= retirar
                repetir = False
            else:
                print("No puedes retirar mas de lo que tienes depositado.")
                print(f"Tu saldo actual es {self.saldo}")

        print(f"Tu saldo es {self.saldo}")


programa()
