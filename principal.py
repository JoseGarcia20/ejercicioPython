import inventario as p1
import carritoCompras as p2

def agregaProducto():
    codigo = input("Ingrese el código del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))

    p1.inventario.agregarProductos(codigo, nombre, precio, cantidad)
    print("El Producto se agrego correctamente al inventario.")

def buscarProductos():
    print("Buscar productos")
    cod = int(input("Ingrese el codigo del producto a buscar: "))
    productoEncontrado = p1.inventario.buscarProductos(cod)
    if productoEncontrado:
        nombre, precio, cantidad = productoEncontrado
        print("Producto encontrado en el sistema")
        print("---------------------------------")
        print("Nombre: ", nombre)
        print("Cantidad: ", precio)
        print("Precio: ", cantidad)
        print("---------------------------------")
    else: 
        print("El producto no se encontro en el sistema.")
    print("")

def mostrarProdcutos():
    print("Lista de Productos")
    p1.inventario.mostrarProdcutos()

def modificarProductos():
    print("Modificar Productos")
    codigo = input("Ingrese el código del producto: ")
    nombre = input("Ingrese el nuevo nombre del producto: ")
    cantidad = int(input("Ingrese la nueva cantidad del producto: "))
    precio = float(input("Ingrese el nuevo valor del producto: "))
    
    p1.inventario.modificarProductos(codigo, nombre, cantidad ,precio)

def agregarCarrito():
    codigo = input("Ingrese el código del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    p2.carroCompras.agregarCarrito(p1.inventario, codigo, cantidad)

def BorrarCarrito():
    codigo = input("Ingrese el código del producto a retirar: ")
    p2.carroCompras.BorrarCarrito(codigo)
    
def ListarCarrito():
    p2.carroCompras.listarCarrito()
    
    
    
    
def menuInventario():
    while True:
        print("---------------------------------")
        print("Menu de Inventario")
        print("1. Agregar Producto.")
        print("2. Buscar Producto.")
        print("3. Mostrar Todos Los Productos.")
        print("4. Modificar Producto.")
        print("5. Salir. ")
        opcion = input("Seleccione una opción: ")
        print("---------------------------------")
    
        if opcion == "1":
            agregaProducto()
        elif opcion == "2":
            buscarProductos()
        elif opcion == "3":
            mostrarProdcutos()
        elif opcion == "4":
            modificarProductos()
        elif opcion == "5":
            print("Saliendo del inventario...")
            break
        else:
            print("La opcion elegida no se encuenta disponible, verifique e intente nuevamente.")
            
def menuCarrito():
    while True:
        print("---------------------------------")
        print("Carrito de compras")
        print("1. Agregar Productos.")
        print("2. Eliminar Producto.")
        print("3. Mostrar carrito.")
        print("4. Salir. ")
        opcion = input("Seleccione una opción: ")
        print("---------------------------------")
    
        if opcion == "1":
            agregarCarrito()
        elif opcion == "2":
            BorrarCarrito()
        elif opcion == "3":
            ListarCarrito()
        elif opcion == "4":
            print("Saliendo de carritode compras...")
            break
        else:
            print("La opcion elegida no se encuenta disponible, verifique e intente nuevamente.")
            
while True:
    print("---------------------------------")
    print("Menu Principal")
    print("1. Administrar Inventario.")
    print("2. Administrar Carrito De Compras.")
    print("3. Salir. ")
    opcion = input("Seleccione una opción: ")
    print("---------------------------------")
    
    if opcion == "1":
        menuInventario()
    elif opcion == "2":
        menuCarrito()
    elif opcion == "3":
        print("Saliendo de la aplicacion...")
        break
    else:
        print("La opcion elegida no se encuenta disponible, verifique e intente nuevamente.")
        
        