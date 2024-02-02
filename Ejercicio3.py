"""3. Teniendo presente el uso y concepto de diccionarios en Python, realizar un
programa con los siguientes requerimientos (4 ptos)
Reglas:
- Crear un diccionario con los keys de nombre, apellidos, edad y dni.
- Pedir por consola los valores para estos keys.
- Mostrar en pantalla sólo los values del diccionario
- Agregar un key adicional con el nombre de “profesion” y un valor para este key
nuevo.
- Eliminar el key dni y mostrar el nuevo diccionario."""

nombre = input("Ingrese su nombre: ")
apellidos = input("Ingrese sus apellidos: ")
edad = input("Ingrese su edad: ")
dni = input("Ingrese su dni: ")

diccionario = {"nombre": nombre, "apellidos": apellidos, "edad": edad, "dni": dni}
print("Mi diccionario es: {}".format(diccionario))

values = list(diccionario.values())
print("Los valores de mi diccionario son: {}".format(values))

diccionario["profesion"] = "Ingeniero de Sistemas"

del diccionario["dni"]
print("Mi diccionario luego de eliminar el DNI de {} {} es el siguiente: {}".format(nombre, apellidos, diccionario))

