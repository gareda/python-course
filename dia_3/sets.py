# mi_set = set([1, 2, 3, 4, 5, (1, 2, 3), 1, 1, 1, 1, 1, 2, 2, 2])
# print(2 in mi_set)

# s1 = {1, 2, 3}
# s2 = {3, 4, 5}
# s3 = s1.union(s2)
# print(s3)

s1 = {1, 2, 3}
s1.add(4)
s1.remove(3)  # Si no hay da error
s1.discard(6)  # Descartar no es lo mismo que eliminar, si no hay no pasa nada
s1.pop()
print(s1)
s1.clear()
print(s1)
