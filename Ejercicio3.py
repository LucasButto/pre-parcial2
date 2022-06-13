'''
## Ejercicio 3

### 3.1 Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Implementar los siguientes métodos:
- Un constructor, donde los datos pueden estar vacíos.
- ``mostrar()``: Muestra los datos de la persona.
- ``esMayorDeEdad()``: Devuelve un valor lógico indicando si es mayor de edad.

### 3.2 Crear una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad 
(es dinero asi que puede tener decimales). El titular será obligatorio y la cantidad es opcional. Implementar los siguientes métodos para la clase:
- Un constructor donde el titular es obligatorio y la cantidad opcional(0 por defecto)
- ``mostrar()``: Muestra los datos de la cuenta.
- ``ingresar(cantidad)``: se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
- ``retirar(cantidad)``: se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

## 3.3 Crear clase CuentaJoven, que deriva de la anterior. Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento. Implementar los siguientes metodos:

- Un constructor con bonificacion opcional(0 por defecto).
- En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo tanto hay que crear un método esTitularValido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.
- Además la retirada de dinero sólo se podrá hacer si el titular es válido.
- El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
'''

class Persona:
    def __init__(self, nombre = "", edad = "", dni= ""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def mostrar(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("DNI: ", self.dni)
    
    def esMayorDeEdad(self):
        if(self.edad >= 18):
            return True
        else:
            return False
    
class Cuenta:
    def __init__(self, titular, cantidad = 0):
        self.titular = titular
        self.cantidad = cantidad
    
    def mostrar(self):
        self.titular.mostrar()
        print("Cantidad: ", self.cantidad)
    
    def ingresar(self, cantidad):
        if(cantidad > 0):
            self.cantidad += cantidad

    def retirar(self, cantidad):
        if(cantidad > 0):
            self.cantidad -= cantidad

Persona1 = Persona("Juan", 10, "12345678")
Persona2 = Persona("Pedro", 20,"87654321")

print("3.1")
print("----------------------------------------------------")
Persona1.mostrar()
print(Persona1.esMayorDeEdad())
print("-----------------------------------------------------")
Persona2.mostrar()
print(Persona2.esMayorDeEdad())
print("-----------------------------------------------------")

Cuenta1 = Cuenta(Persona2, 100)

print("3.2")
print("----------------------------------------------------")
Cuenta1.mostrar()
print("-----------------------------------------------------")
ingreso=100
print("Ingreso de plata: $",ingreso)
Cuenta1.ingresar(ingreso)
Cuenta1.mostrar()
print("-----------------------------------------------------")
retiro=50
print("Retiro de plata: $",retiro)
Cuenta1.retirar(retiro)
Cuenta1.mostrar()