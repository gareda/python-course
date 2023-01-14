class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nadico")


class Pajaro(Animal):
    pass


piolin = Pajaro(2, "Amarillo")

print(piolin.color)
