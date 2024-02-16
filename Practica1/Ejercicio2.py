"""2.Usando el concepto y funciones de listas, realizar un programa con
las siguiente características (3 ptos):
Reglas:
- Crear una lista con 10 valores random o aleatorios (Pista: Usar el método
append y for)
- Llenar otra lista con sus cubos.
- Llenar una lista nueva con sus cuadrados.
- Mostrar de manera inversa la suma de ambas listas creadas."""

import random

lista = []
for _ in range(10):
    lista.append(random.randint(1, 50))
    cubos = [valor ** 3 for valor in lista]
    cuadrados = [valor ** 2 for valor in lista]

print("La lista de los 10 valores aleatorios es: {}".format(lista))
print("La lista de cubos de los 10 valores aleatorios es: {}".format(cubos))
print("La lista de cuadrados de los 10 valores aleatorios es: {}".format(cuadrados))

inversa = sum(cubos[::-1]) + sum(cuadrados[::-1])
print("Suma inversa de las listas creadas: {}".format(inversa))
