"""
En El Salvador, los comerciantes de mercados locales desean llevar un
control organizado de sus ventas diarias. Cada venta incluye tipos variados
de productos con ciertas características y precios ya definidos. Sin un registro,
es difícil saber cuáles productos generan más ingresos y cómo planificar el
inventario de manera eficiente.
Se busca un sistema que permita registrar las ventas realizadas, calcular
automáticamente los ingresos totales y por producto, y generar una salida
en pantalla al final que muestre los datos ordenados por ingreso o por
cantidad vendida. 
"""

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
