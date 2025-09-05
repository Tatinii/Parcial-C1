

#Clases
class Producto:
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

#Funciones
def menu():
    print("1. Ingresar venta")
    print("2. Mostrar reporte de ventas")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion



#Final
while True:
    opcion = menu()
    if opcion == "1":
        print("Función para ingresar venta (pendiente de implementar)")
    elif opcion == "2":
        print("Función para mostrar reporte de ventas (pendiente de implementar)")
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, intente de nuevo.")
