def indefinida(*args):
    anterior = 1

    for n in args:
        if anterior == 0 and n == 0:
            return True
        anterior = n
    return False


print(indefinida(5, 6, 1, 0, 0, 9, 3, 5))
# print(indefinida(6, 0, 5, 1, 0, 3, 0, 1))
