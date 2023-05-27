def DecoradorInventario(cls):
    
    @classmethod
    def modificarProductos(cls, codigo, nombre, cantidad, precio):
        for producto in cls.invArticulos:
            if producto["Codigo"] == codigo:
                producto["Nombre"] = nombre
                producto["Cantidad"] = cantidad
                producto["Precio"] = precio
                print("Producto modificador en el inventario.")
                return
        print("El producto no fue encontrado en el inventario.")
    
    cls.modificarProductos = modificarProductos
    return cls

@DecoradorInventario
class inventario:
    
    invArticulos = []
    
    def __init__(self, codigo, nombre, precio, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    
    @classmethod
    def agregarProductos(cls, codigo, nombre, precio, cantidad):
        productos = {"Codigo":codigo,"Nombre":nombre,"Precio":precio,"Cantidad":cantidad}
        cls.invArticulos.append(productos)
    
    @classmethod
    def buscarProductos(cls, codigo):
        for pro in cls.invArticulos:
            if pro["Codigo"] == codigo:
                return pro["Nombre"], pro["Precio"], pro["Cantidad"]
        return None
    
    @classmethod
    def mostrarProdcutos(cls):
        for pro in cls.invArticulos:
            print("---------------------------------------------")
            print("Codigo: ", pro["Codigo"])
            print("Nombre: ", pro["Nombre"])
            print("Precio: ", pro["Precio"])
            print("Cantidad: ", pro["Cantidad"])
            print("---------------------------------------------")


