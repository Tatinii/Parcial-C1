from datetime import datetime

#Clases
#  clase para manejar productos con existencias
class Producto:
    def __init__(self, nombre, categoria, precio, existencia):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.existencia = existencia
        
#  clase para manejar ventas
class Venta:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad
        self.total = producto.precio * cantidad
        self.fecha = datetime.now()

#Funciones

#Funcion para mostrar el menú y obtener la opción del usuario
def menu():
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Ingresar venta")
    print("2. Mostrar reporte de ventas")
    print("3. Agregar nuevo producto")
    print("4. Ver inventario actual")
    print("5. Salir")
    return input("Seleccione una opción: ")

#Lista inicial de productos y ventas
productos = [
    Producto("Tomate", "Verdura", 0.25, 100),
    Producto("Manzana", "Fruta", 0.30, 150),
    Producto("Pan", "Panadería", 0.15, 200),
    Producto("Leche", "Lácteos", 1.25, 50)
]
# Lista para almacenar ventas
ventas = []

# Función para agregar un nuevo producto
def agregar_producto():
    print("\n=== AGREGAR NUEVO PRODUCTO ===")
    # Validaciones de entrada
    try:
        nombre = input("Ingrese el nombre del producto: ").strip()
        if not nombre:
            print("Error: El nombre no puede estar vacío")
            return
        
        # Verificar si el producto ya existe
        if any(p.nombre.lower() == nombre.lower() for p in productos):
            print("Error: Este producto ya existe")
            return
        
        categoria = input("Ingrese la categoría del producto: ").strip()
        if not categoria:
            print("Error: La categoría no puede estar vacía")
            return
        
        precio = float(input("Ingrese el precio del producto: $"))
        if precio <= 0:
            print("Error: El precio debe ser mayor que 0")
            return
        if precio > 1000:  # Precio máximo razonable
            print("Error: El precio parece ser demasiado alto")
            return
            
        existencia = int(input("Ingrese la cantidad en existencia: "))
        if existencia < 0:
            print("Error: La existencia no puede ser negativa")
            return
        
        nuevo_producto = Producto(nombre, categoria, precio, existencia)
        productos.append(nuevo_producto)
        print(f"\nProducto '{nombre}' agregado exitosamente")
        
    except ValueError as e:
        print("Error: Ingrese valores numéricos válidos")
    except Exception as e:
        print(f"Error inesperado: {str(e)}")

# Función para ingresar una venta
def ingresar_venta():
    print("\nProductos disponibles:")
    for i, producto in enumerate(productos, 1):
        print(f"{i}. {producto.nombre} - ${producto.precio} (Disponible: {producto.existencia})")
# Validaciones de entrada
    try:
        seleccion = int(input("\nSeleccione el número del producto: ")) - 1
        if 0 <= seleccion < len(productos):
            cantidad = int(input("Ingrese la cantidad: "))
            if cantidad <= 0:
                print("Error: La cantidad debe ser mayor a 0")
                return
                
            if cantidad > productos[seleccion].existencia:
                print("Error: No hay suficiente existencia")
                return

            # Restar la cantidad vendida de la existencia    
            productos[seleccion].existencia -= cantidad
            venta = Venta(productos[seleccion], cantidad)
            ventas.append(venta)
            print(f"Venta registrada: {cantidad} {productos[seleccion].nombre}")
            print(f"Existencia restante: {productos[seleccion].existencia}")
        else:
            print("Selección inválida")
    except ValueError:
        print("Error: Ingrese un número válido")

def mostrar_inventario():
    print("\n=== INVENTARIO ACTUAL ===")
    print(f"{'Producto':<15} {'Categoría':<15} {'Precio':<10} {'Existencia':<10}")
    print("-" * 50)
    for producto in sorted(productos, key=lambda x: x.nombre):
        print(f"{producto.nombre:<15} {producto.categoria:<15} ${producto.precio:>7.2f} {producto.existencia:>10}")

def mostrar_reporte():
    if not ventas:
        print("\nNo hay ventas registradas")
        return

    print("\nReporte de Ventas")
    items_ordenados = sorted(reporte.items(),
                           key=lambda x: x[1]['total'],
                           reverse=True)
    print("=" * 75)
    
    # Diccionario para acumular ventas por producto
    reporte = {}
    for venta in ventas:
        if venta.producto.nombre in reporte:
            reporte[venta.producto.nombre]['cantidad'] += venta.cantidad
            reporte[venta.producto.nombre]['total'] += venta.total
            reporte[venta.producto.nombre]['existencia'] = venta.producto.existencia
        else:
            reporte[venta.producto.nombre] = {
                'cantidad': venta.cantidad,
                'total': venta.total,
                'existencia': venta.producto.existencia
            }
    
    # Ordenar por total de ventas
    items_ordenados = sorted(reporte.items(), 
                           key=lambda x: x[1]['total'], 
                           reverse=True)
    
    total_general = 0
    print(f"{'Producto':<15} {'Cantidad':<10} {'Total':<10} {'Existencia':<10} {'Última Venta'}")
    print("-" * 75)
    for producto, datos in items_ordenados:
        ultima_venta = max((v.fecha for v in ventas if v.producto.nombre == producto))
        print(f"{producto:<15} {datos['cantidad']:<10} ${datos['total']:>7.2f} {datos['existencia']:<10} {ultima_venta.strftime('%d/%m/%Y %H:%M')}")
        total_general += datos['total']
    
    print("-" * 75)
    print(f"Total General: ${total_general:.2f}")

# while para controlar el menu principal
while True:
    opcion = menu()
    if opcion == "1":
        ingresar_venta()
    elif opcion == "2":
        mostrar_reporte()
    elif opcion == "3":
        agregar_producto()
    elif opcion == "4":
        mostrar_inventario()
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, intente de nuevo.")
