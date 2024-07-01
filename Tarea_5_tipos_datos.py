# Programa: Gestión básica de información de un vehículo
# Descripción: Este programa permite gestionar información básica de un vehículo,
# incluyendo modelo, año de fabricación y precio.

def main():
    # Datos del vehículo
    modelo = "Sedan"
    año_fabricacion = 2023
    precio = 25000.50
    disponible = True

    # Mostrar información del vehículo
    print("Información del vehículo:")
    print(f"Modelo: {modelo}")
    print(f"Año de fabricación: {año_fabricacion}")
    print(f"Precio: ${precio}")
    print(f"Disponible: {'Sí' if disponible else 'No'}")

if __name__ == "__main__":
    main()





