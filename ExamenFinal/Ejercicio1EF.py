

import random


def lista_aleatoria():
    lista = [random.randint(1, 100) for _ in range(10)]
    print("La lista aleatoria generada es la siguiente:", lista)
    return lista


def eliminarrepetidos(lista):
    lista_sin_repetidos = list(set(lista))
    print("La lista sin números repetidos es:", lista_sin_repetidos)
    return lista_sin_repetidos


def ordenarlista(lista):
    descendente = sorted(lista, reverse=True)
    ascendente = sorted(lista)
    print("La lista ordenada de mayor a menor es:", descendente)
    print("La lista ordenada de menor a mayor es:", ascendente)
    return descendente, ascendente


def mayornumeropar(lista):
    numerospares = [num for num in lista if num % 2 == 0]
    mayorpar = max(numerospares)
    print("******************************************************************")
    print("Mayor número par de la lista:", mayorpar)
    return mayorpar


lista_aleatoria = lista_aleatoria()
lista_sin_repetidos = eliminarrepetidos(lista_aleatoria)
lista_descendente, lista_ascendente = ordenarlista(lista_sin_repetidos)
mayorpar = mayornumeropar(lista_sin_repetidos)
