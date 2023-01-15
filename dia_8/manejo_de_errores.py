# def suma():
#     n1 = int(input("numero 1: "))
#     n2 = int(input("numero 2: "))
#     print(n1 + n2)
#     print("Gracias por sumar")
#
# """
# try:
#     # CODIGO QUE QUEREMOS PROBAR
# except:
#     # CODIGO A EJECUTAR SI HAY UN ERROR
# else:
#     # CODIGO A EJECUTAR SI NO HAY UN ERROR
# finally:
#     # CODIGO QUE SE VA A EJECUTAR DE TODOS MODOS
# """
#
# try:
#     suma()
# # except:
# #     print("Algo no ha salido bien")
# except TypeError:
#     print("Estas intentando concatenar tipos distintos")
# except ValueError:
#     print("Ese no es un número")
# else:
#     print("Hicistetodo bien")
# finally:
#     print("Eso fuetodo")

def pedir_numero():
    while True:
        try:
            numbero = int(input("Dame un número: "))
        except:
            print("Ese no es un número")
        else:
            print(f"Ingresaste el número {numbero}")
            break

    print("Gracias")


pedir_numero()
