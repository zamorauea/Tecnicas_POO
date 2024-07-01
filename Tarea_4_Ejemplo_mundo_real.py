# cliente.py

class Cliente:
    def __init__(self, nombre, documento_identidad, email):
        self.nombre = nombre
        self.documento_identidad = documento_identidad
        self.email = email

    def __str__(self):
        return f"Cliente: {self.nombre}, ID: {self.documento_identidad}, Email: {self.email}"


# habitacion.py

class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.ocupada = False

    def reservar(self):
        if not self.ocupada:
            self.ocupada = True
            return True
        return False

    def liberar(self):
        if self.ocupada:
            self.ocupada = False

    def __str__(self):
        estado = "Ocupada" if self.ocupada else "Disponible"
        return f"Habitación {self.numero}: Tipo {self.tipo}, Precio {self.precio}, Estado: {estado}"


# reserva.py

class Reserva:
    def __init__(self, cliente, habitacion, dias):
        self.cliente = cliente
        self.habitacion = habitacion
        self.dias = dias
        self.confirmada = False

    def confirmar_reserva(self):
        if self.habitacion.reservar():
            self.confirmada = True
            return True
        return False

    def cancelar_reserva(self):
        if self.confirmada:
            self.habitacion.liberar()
            self.confirmada = False

    def __str__(self):
        estado = "Confirmada" if self.confirmada else "Pendiente"
        return f"Reserva para {self.cliente.nombre}: Habitación {self.habitacion.numero}, Días: {self.dias}, Estado: {estado}"




def main():
    cliente1 = Cliente("Juan Pérez", "12345678", "juan@example.com")
    habitacion1 = Habitacion(101, "Doble", 100)

    reserva1 = Reserva(cliente1, habitacion1, 3)

    print(cliente1)
    print(habitacion1)

    if reserva1.confirmar_reserva():
        print("Reserva confirmada:")
    else:
        print("No se pudo confirmar la reserva:")

    print(reserva1)

    reserva1.cancelar_reserva()
    print("Reserva cancelada:")
    print(habitacion1)
    print(reserva1)


if __name__ == "__main__":
    main()

