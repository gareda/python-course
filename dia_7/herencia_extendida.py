"""
class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nadico")

    def hablar(self):
        print("Este animal emite un sonido")


class Pajaro(Animal):
    def __init__(self, edad, color, altura_vuelo):
        # self.color = color # Atributos heredados de Animal
        # self.edad = edad
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print("pio")

    def volar(self, metros):
        print(f"El pajaro vuela {metros} metros")


piolin = Pajaro(3, "amarillo", 60)
mi_animal = Animal(5, "negro")

piolin.hablar()
"""


class Padre:
    def hablar(self):
        print("Hola")


class Madre:
    def reir(self):
        print("Jaja")

    def hablar(self):
        print("Que tal")


class Hijo(Padre, Madre):  # El orden establece prioridad de metodos
    pass


class Nieto(Hijo):
    pass


mi_nieto = Nieto()
mi_nieto.hablar()
mi_nieto.reir()
print(Nieto.__mro__)