from pathlib import Path
from os import system


def programa():
    ruta = ruta_recetas()
    recetas = contar_total_recetas(ruta)
    opciones = {
        1: "Leer una receta",
        2: "Crear una receta",
        3: "Eliminar una receta",
        4: "Crear una categoría",
        5: "Eliminar una categoría",
        6: "Finalizar el programa"
    }

    saludar(ruta, recetas)

    while True:
        opcion = menu(opciones)

        match opcion:
            case 1:
                leer_receta(ruta)
                input("\n(Pulsa cualquier intro para volver a manu inicial)")
            case 2:
                crear_receta(ruta)
            case 3:
                eliminar_receta(ruta)
            case 4:
                crear_categoria(ruta)
            case 5:
                eliminar_categoria(ruta)
            case 6:
                break

        system("cls")


def ruta_recetas():
    ruta = Path(Path.cwd(), "recetas")

    return ruta


def contar_total_recetas(ruta):
    cantidad = 0

    for receta in Path(ruta).glob("**/*.txt"):
        cantidad += 1

    return cantidad


def saludar(ruta, recetas):
    print(
        "Bienvenido a recetario interactivo."
        f"\nActalmente hay {recetas} en la ruta: {ruta}"
    )


def menu(opciones):
    validacion = False

    while not validacion:
        imprimir_menu(opciones)
        opcion = solicitar_opcion("opción")
        validacion = validar_opcion(opciones, opcion)

    return int(opcion)


def imprimir_menu(opciones):
    for posicion, opcion in opciones.items():
        print(f"[{posicion}] - {opcion}")


def contar_opciones(ruta, categoria=""):
    opciones = {}
    contador = 0

    if categoria == "":
        posibilidades = Path(ruta).iterdir()
    else:
        posibilidades = Path(ruta, categoria).glob("*.txt")

    for opcion in posibilidades:
        contador += 1
        opciones[contador] = opcion.stem

    return opciones


def solicitar_opcion(tipo):
    return input(f"¿Que {tipo} quieres escoger?: ")


def validar_opcion(opciones, opcion):
    if not opcion.isalpha():
        if len(opcion) == 1:
            if int(opcion) in opciones:
                return True

    print("Debes introducion una opcion valida.")
    return False


def seleccionar_catagoria(ruta):
    categorias = contar_opciones(ruta)
    eleccion = menu(categorias)
    return int(eleccion), categorias


def seleccionar_receta(ruta):
    categoria, categorias = seleccionar_catagoria(ruta)

    recetas = contar_opciones(ruta, categorias[categoria])
    receta = menu(recetas)

    ruta = Path(ruta, categorias[categoria], recetas[receta] + ".txt")
    return ruta


def leer_receta(ruta):
    receta = seleccionar_receta(ruta)
    contenido = (open(receta)).read()
    print(contenido)


def crear_receta(ruta):
    repetir = True

    categoria, categorias = seleccionar_catagoria(ruta)

    while repetir:
        nombre = input("Nombre receta: ")
        receta = Path(ruta, categorias[categoria], nombre + ".txt")

        if not receta.exists():
            descripcion = input("Descripcion receta: ")
            receta = open(receta, "x")
            receta.write(descripcion)
            receta.close()
            repetir = False
        else:
            print("Esta ya existe, intentalo con otro nombre.")


def eliminar_receta(ruta):
    receta = seleccionar_receta(ruta)
    receta.unlink()


def crear_categoria(ruta):
    repetir = True

    while repetir:
        nombre = input("Nueva categoria: ")
        categoria = Path(ruta, nombre)

        if not categoria.exists():
            categoria.mkdir()
            repetir = False
        else:
            print("Esta ya existe, intentalo con otro nombre.")


def eliminar_categoria(ruta):
    categoria, categorias = seleccionar_catagoria(ruta)
    ruta = Path(ruta, categorias[categoria])
    ruta.rmdir()


programa()
