""""
3. Escribir un programa para gestionar los errores en Python (3 ptos):
Reglas:
- El programa deberá tener una función para ingresar dos datos
por consola.
- Deberá tener una función en el caso haya una división entre cero
mencionar el error.
- Deberá tener una función la cuál evaluará la suma de datos
incorrectos, mencionar el error
- Deberá tener una función donde se ingresarán N datos a una lista y al
momento de pedir un índice incorrecto para mostrarlo en consola y no
exista respectivamente ese índice, aplicar try, except
respectivamente.
- Todas las funciones creadas tendrán la facultad de volver a pedir el
número hasta que se ingresen correctamente."""

def ingresar_datos():
    while True:
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            return num1, num2
        except ValueError:
            print("Error")

def division_cero(num1, num2):
    try:
        result = num1 / num2
        print("El resultado de la división es: ", result)
    except ZeroDivisionError:
        print("No se puede dividir entre cero")

def evaluar_suma_datos_incorrectos(num1,num2):
    suma = num1+num2
    return suma

def datos_lista():
    lista = []
    while True:
        try:
            dato = int(input("Ingrese un dato para la lista (0 para terminar): "))
            if dato == 0:
                break
            lista.append(dato)
        except ValueError:
            print("Error")

    while True:
        try:
            indice = int(input("Ingrese un índice para mostrar el dato de la lista: "))
            dato = lista[indice]
            print("El dato en el índice {} es: {}".format(indice,dato))
            break
        except IndexError:
            print("Error: El índice ingresado está fuera del rango de la lista.")

print("1. División entre dos números.")
print("2. Evaluar la suma de datos incorrectos.")
print("3. Ingresar datos a una lista y mostrar un índice.")
opcion = int(input("Seleccione una opción: "))

if opcion == 1:
    num1, num2 = ingresar_datos()
    division_cero(num1, num2)
elif opcion == 2:
    num1, num2 = ingresar_datos()
    suma = evaluar_suma_datos_incorrectos(num1,num2)
elif opcion == 3:
    datos_lista()
else:
    print("Ingrese los números que se ven en pantalla")
