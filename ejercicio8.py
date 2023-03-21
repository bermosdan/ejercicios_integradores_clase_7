class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.__cantidad = cantidad

    @property
    def titular(self):
        return self.__titular
    
    @property
    def cantidad(self):
        return self.__cantidad
    
    @titular.setter
    def titular(self, titular):
        self.__titular = titular
    
    def mostrar(self):
        return "Cuenta\n" + "Titular: " + self.titular + " - Cantidad: " + str(self.cantidad)
    
    def ingresar(self,cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad + cantidad
    
    def retirar(self,cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad - cantidad

class CuentaJoven(Cuenta):
    def __init__(self,titular,edad, cantidad=0,bonificacion=0):
        super().__init__(titular,cantidad)
        self.edad=edad
        self.bonificacion=bonificacion
    
    @property
    def bonificacion(self):
        return self.__bonificacion
    
    @property
    def edad(self):
        return self.__edad
    
    @bonificacion.setter
    def bonificacion(self,bonificacion):
        self.__bonificacion=bonificacion

    @edad.setter
    def edad(self,edad):
        self.__edad=edad

    def mostrar(self):
        return "Cuenta Joven\n" + "Titular:" + self.titular + " - Cantidad:" + str(self.cantidad) + "- Bonificación:" + str(self.bonificacion) + "%"
   
    def esTitularValido(self):
        return self.edad < 25 and self.edad > 18
    
    def retirar(self,cantidad):
        if not self.esTitularValido():
            print ("No puesdes retirar el dinero. titular no válido")
        elif cantidad > 0:
            super().retirar(cantidad)

c1 = CuentaJoven("Oscar Bernal", 21, 12550.50, 10)
print(c1.mostrar())
c1.retirar(50000)
print(c1.mostrar())

c2 = CuentaJoven("Jose Perez", 29, 12550.50, 20)
print(c2.mostrar())
c2.retirar(50000)
print(c2.mostrar())

c3 = CuentaJoven("Maria Sanchez", 17, 12550.50, 30)
print(c3.mostrar())
c3.retirar(50000)
print(c3.mostrar())