"""
1. Escriba un programa donde tendrá los siguientes requisitos (4 ptos):
Reglas:
- Crear una clase llamada Persona donde sus atributos deben ser nombre,
edad, saldo y de nacionalidad peruana (use el manejo de errores para el
tipo de dato) y un método para solicitar su nombre y edad.
- Tendrá un método cumpleaños donde cada vez que invoque aumentará en
un año la edad de la persona.
- Crear la instancia de la clase Persona y usar su método cumpleaños para
incrementar su edad (mínimo instanciar la clase 2 veces, mostrar por
pantalla dicha edad actualizada).
- Crear una función que retorne solamente la fecha, hora y minuto que se ha
registrado esta persona (Mostrar por pantalla este valor)
"""

from datetime import datetime

class Persona:
    def __init__(self, nombre, edad, saldo):
        self.nombre = nombre
        self.edad = edad
        self.saldo = saldo
        self.nacionalidad = "Peruana"

    def solicitar_su_nombre_y_edad(self):
        self.nombre = input("Ingrese su nombre: ")
        while True:
            try:
                edad_consola= int(input("Ingrese su edad: "))
                if edad_consola < 0:
                    raise ValueError("Ingrese un número positivo")
                self.edad = edad_consola
                break
            except (ValueError, TypeError) as e:
                print("Error:", e)
    def cumpleaños(self):
        self.edad += 1

def fecha():
    fecha_actual = datetime.now()
    return fecha_actual.strftime("%Y-%m-%d %H:%M")


nombre_u = input("Ingrese el nombre de la persona: ")

while True:
    try:
        edad_u = int(input("Ingrese la edad de la persona: "))
        if edad_u< 0:
            print("Ingrese un número positivo")
        break
    except (ValueError, TypeError) as e:
        print("Error:", e)

saldo_u = float(input("Ingrese el saldo de la persona: "))

persona = Persona(nombre_u, edad_u, saldo_u)

persona.cumpleaños()

print(f"La nueva edad de {persona.nombre} es: {persona.edad}")

fecha_hora_registro = fecha()
print("La fecha y hora de registro es: {}".format(fecha_hora_registro))


