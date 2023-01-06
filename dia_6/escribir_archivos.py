archivo = open("prueba1.txt", "a") # mode w: sobre escribe el texto, "a" lo añade al final

# lista = ["hola", "mundo", "aqui", "estoy"]
#
# for p in lista:
#     archivo.writelines(p + "\n")

archivo.write("bienvenido")

archivo.close()
