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
            
c1 = Cuenta("Oscar Bernal", 1250.50)
print(c1.mostrar())
c1.ingresar(100000.21)
print(c1.mostrar())
c1.retirar(1250.11)
print(c1.mostrar())
c1.ingresar(-100000)
print(c1.mostrar())
c1.retirar(100001)
print(c1.mostrar())

