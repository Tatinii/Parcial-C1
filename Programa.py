

#Clases
class Producto:
    def __init__(self, nombre, categoria, precio, existencia):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.existencia = existencia
        

class Venta:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad
        self.total = producto.precio * cantidad

#Funciones
def menu():
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Ingresar venta")
    print("2. Mostrar reporte de ventas")
    print("3. Agregar nuevo producto")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

def agregar_producto():
    print("\n=== AGREGAR NUEVO PRODUCTO ===")
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
        
        nuevo_producto = Producto(nombre, categoria, precio)
        productos.append(nuevo_producto)
        print(f"\nProducto '{nombre}' agregado exitosamente")
        
    except ValueError:
        print("Error: El precio debe ser un número válido")
    except Exception as e:
        print(f"Error inesperado: {str(e)}")

# Lista para almacenar productos y ventas
productos = [
    Producto("Tomate", "Verdura", 0.25),
    Producto("Manzana", "Fruta", 0.30),
    Producto("Pan", "Panadería", 0.15),
    Producto("Leche", "Lácteos", 1.25)
]
ventas = []

def ingresar_venta():
    print("\nProductos disponibles:")
    for i, producto in enumerate(productos, 1):
        print(f"{i}. {producto.nombre} - ${producto.precio}")
    
    try:
        seleccion = int(input("\nSeleccione el número del producto: ")) - 1
        if 0 <= seleccion < len(productos):
            cantidad = int(input("Ingrese la cantidad: "))
            if cantidad > 0:
                venta = Venta(productos[seleccion], cantidad)
                ventas.append(venta)
                print(f"Venta registrada: {cantidad} {productos[seleccion].nombre}")
            else:
                print("La cantidad debe ser mayor a 0")
        else:
            print("Selección inválida")
    except ValueError:
        print("Error: Ingrese un número válido")

def mostrar_reporte():
    if not ventas:
        print("\nNo hay ventas registradas")
        return

    print("\nReporte de Ventas")
    print("=" * 50)
    
    # Diccionario para acumular ventas por producto
    reporte = {}
    for venta in ventas:
        if venta.producto.nombre in reporte:
            reporte[venta.producto.nombre]['cantidad'] += venta.cantidad
            reporte[venta.producto.nombre]['total'] += venta.total
        else:
            reporte[venta.producto.nombre] = {
                'cantidad': venta.cantidad,
                'total': venta.total
            }
    
    # Ordenar por total de ventas
    items_ordenados = sorted(reporte.items(), 
                           key=lambda x: x[1]['total'], 
                           reverse=True)
    
    total_general = 0
    print(f"{'Producto':<15} {'Cantidad':<10} {'Total':<10}")
    print("-" * 50)
    for producto, datos in items_ordenados:
        print(f"{producto:<15} {datos['cantidad']:<10} ${datos['total']:.2f}")
        total_general += datos['total']
    
    print("-" * 50)
    print(f"Total General: ${total_general:.2f}")

# Modificar el while principal
while True:
    opcion = menu()
    if opcion == "1":
        ingresar_venta()
    elif opcion == "2":
        mostrar_reporte()
    elif opcion == "3":
        agregar_producto()
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, intente de nuevo.")
