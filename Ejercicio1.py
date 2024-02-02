"""1. Usando los tipos de datos y sus conversiones realizar lo siguiente. (3 ptos)
Reglas:
- Pedir por consola nombre y edad de un usuario.
- Edad tiene que ser tipo entero, para esto apoyarse de la conversión de datos
- Identificar los tipos de datos ingresados y mostrarlos en pantalla.
- Pedir los nombres y edades para dos trabajadores y finalmente
agregarlos a una lista. Mostrar la suma de las edades de los
trabajadores localizándolos por la posición en la lista."""

nom1 = input("Ingrese su nombre: ")
edad1 = int(input("Ingrese su edad: "))

print("El tipo de dato de {} es: {}".format(nom1, (type(nom1))))
print("El tipo de dato de {} es: {}".format(edad1, (type(edad1))))

nom2 = input("Ingrese su nombre: ")
edad2 = int(input("Ingrese su edad: "))

print("El tipo de dato de {} es: {}".format(nom2, (type(nom2))))
print("El tipo de dato de {} es: {}".format(edad2, (type(edad2))))

mi_lista = [(nom1, edad1), (nom2, edad2)]

suma = mi_lista[0][1] + mi_lista[1][1]
print("La suma de las edades de ambos trabajadores es: {}".format(suma))
