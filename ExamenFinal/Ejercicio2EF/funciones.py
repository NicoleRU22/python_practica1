# funciones.py

import math

def crear_archivo():
    with open("notas.txt", "a+") as archivo:
        archivo.write("")

def escribir_tamaño_lista(tamaño_lista):
    with open("notas.txt", "a") as archivo:
        archivo.write(f"Tamaño de la lista: {tamaño_lista}\n")

def calcular_raiz_cuadrada():
    with open("notas.txt", "r") as archivo:
        contenido = archivo.readlines()

    numeros = [int(linea.split(":")[1]) for linea in contenido if "Tamaño de la lista" in linea]

    with open("notas.txt", "a") as archivo:
        archivo.write("Raíces cuadradas:\n")
        for numero in numeros:
            raiz_cuadrada = math.sqrt(numero)
            archivo.write(f"{raiz_cuadrada}\n")
