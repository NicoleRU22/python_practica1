"""
2. Usando el concepto de herencia y encapsulación (para saldo) para crear
elsiguiente programa (3 ptos):
Reglas:
- Agregar un atributo saldo a la clase persona (ejercicio anterior).
- Crear un método transferencia y mostrar saldo (mostrará el saldo actual
que tiene la persona) para la clase mencionada
- El método transferencia hace que la Persona que llame al método pueda
transferir la cantidad monto al objeto Persona2 por consiguiente deberá
ir actualizando también el saldo o monto que tiene la otra persona en su
cuenta cada vez que use el método transferencia

- Comprobar si no se tiene dinero suficiente no se ejecuta la acción e
imprimir “Saldo insuficiente”. Comprobar instanciado la clase por lo
menos realizando una transferencia y con dos personas.
"""
class Persona:
    def __init__(self, nombre, edad, saldo):
        self.nombre = nombre
        self.edad = edad
        self.__saldo = saldo

    def saldo(self):
        return self.__saldo

    def transferencia(self, monto, transferir_persona):
        if monto <= self.__saldo:
            self.__saldo -= monto
            transferir_persona.__saldo += monto
            print("Se logró realizar su transferencia de manera exitosa")
        else:
            print("Saldo insuficiente para realizar la transferencia")

persona1 = Persona("Nicole", 18, 2000)
persona2 = Persona("Alexandra", 20, 1500)

monto_transferencia = 500
persona1.transferencia(monto_transferencia, persona2)

print(f"Saldo de {persona1.nombre} es: {persona1.saldo()}")
print(f"Saldo de {persona2.nombre} es: {persona2.saldo()}")
