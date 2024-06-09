from abc import ABC, abstractmethod


class Vehiculo(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass

    @abstractmethod
    def acelerar(self):
        pass


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, combustible):
        super().__init__(marca, modelo)
        self.__combustible = combustible  # Atributo privado

    def encender(self):
        if self.__combustible > 0:
            print(f"El {self.marca} {self.modelo} está encendido.")
        else:
            print("No hay combustible.")

    def apagar(self):
        print(f"El {self.marca} {self.modelo} está apagado.")

    def acelerar(self):
        if self.__combustible > 0:
            self.__combustible -= 1
            print(f"El {self.marca} {self.modelo} está acelerando.")
        else:
            print("No hay suficiente combustible.")

    def obtener_combustible(self):
        return self.__combustible


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def encender(self):
        print(f"La motocicleta {self.marca} {self.modelo} está encendida.")

    def apagar(self):
        print(f"La motocicleta {self.marca} {self.modelo} está apagada.")

    def acelerar(self):
        print(f"La motocicleta {self.marca} {self.modelo} está acelerando.")
def manejar_vehiculo(vehiculo):
    vehiculo.encender()
    vehiculo.acelerar()
    vehiculo.apagar()

# Creamos instancias de Automovil y Motocicleta
automovil = Automovil("Chevrolet", "Corolla", 10)
motocicleta = Motocicleta("Harley-Davidson", "Sportster", "Crucero")

# Aplicamos polimorfismo
manejar_vehiculo(automovil)
manejar_vehiculo(motocicleta)
