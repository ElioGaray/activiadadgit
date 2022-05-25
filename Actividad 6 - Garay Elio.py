"""Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad 
(puede tener decimales). El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos
para la clase: 

Un constructor.
mostrar(): Muestra los datos de la cuenta. 
ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada. 
retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos"""

#Clase
class Cuenta:
    
    #Constructor
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad

    #Métodos
    def mostrar(self):
        print(f"\nEl titular {self.titular} tiene ${self.cantidad:.2f} actualmente en su cuenta")
    
    def ingresar(self, num):
        if num >= 0:
            self.cantidad = self.cantidad + num
        else:
            print(f"\nEsta operación no se pudo llevar a cabo, ya que el valor {num} es incorrecto")

    def retirar(self, num):
        self.cantidad = self.cantidad - num


#Ingreso de datos iniciales para crear el objeto
print("\n\t--Ingreso de datos---")
nombre_titular = input("Ingrese el nombre y apellido del titular de la cuenta: ")
cantidad_cuenta = float(input(f"Ingrese la cantidad de dinero que tiene en la cuenta {nombre_titular}, por favor: $"))

#Creo el objeto
cuenta1 = Cuenta(nombre_titular, cantidad_cuenta)

#LLamo a la función mostrar
cuenta1.mostrar()

#--------------------------------------------------------------------------------------

#Ingreso del valor a ingresar en la cuenta
print("\n\t--Ingreso de valores---")
numero = float(input("Ingrese la cantidad de dinero que desea ingresar a la cuenta: $"))

#LLamo a la función ingresar
cuenta1.ingresar(numero)

#LLamo a la función mostrar
cuenta1.mostrar()

#--------------------------------------------------------------------------------------

#Ingreso del valor a retirar en la cuenta
print("\n\t--Ingreso de valores---")
numero = float(input("Ingrese la cantidad de dinero que desea retirar de la cuenta: $"))

#Llamo a la función retirar
cuenta1.retirar(numero)

#LLamo a la función mostrar
cuenta1.mostrar()


