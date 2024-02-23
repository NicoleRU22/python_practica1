import time

def medir_tiempo_sumar(func):
    def decorador(*args, **kwargs):
        comienzo = time.time()
        result = func(*args, **kwargs)
        final = time.time()
        tiempo = final - comienzo
        print(f"Tiempo de ejecución: {tiempo} segundos")
        return result
    return decorador

def multiplicacion(a, b, c, d):
    return a * b * c * d

resultado = multiplicacion(2, 3, 4, 5)
print("El resultado es:", resultado)

