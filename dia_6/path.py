from pathlib import Path

"""
base = Path.home()
guia = Path(base, "Europa", "España", Path("Barcelona", "Sagrada_Familia.txt"))
guia2 = guia.with_name("La_Pedrera.txt")
print(guia)
print(guia2)
print(guia.parent)
print(guia.parent.parent)
"""

# guia = Path(Path.home(), "Desktop", "Python", "Dia 6")
# for txt in Path(guia).glob("*.py"):
#     print(txt)

guia = Path("Europam", "España", "Barcelona", "Sagrada_Familia.txt")
en_europa = guia.relative_to(Path("Europa"))
en_espania = guia.relative_to(Path("Europa", "España"))
print(en_europa)
print(en_espania)
