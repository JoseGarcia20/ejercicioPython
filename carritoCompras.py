class carroCompras:
    
    carritoCompras = []
    
    @classmethod
    def agregarCarrito(cls, inventario, codigo, cantidad):
        producto = inventario.buscarProductos(codigo)
        if producto:
            cls.carritoCompras.append({"Codigo": codigo, "Cantidad": cantidad})
            print("Se agrego de manera correcta el producto al carrito.")
        else:
            print("El producto no existe en el inventario.")
    
    @classmethod
    def BorrarCarrito(cls, codigo):
        for producto in cls.carritoCompras:
            if producto["Codigo"] == codigo:
                cls.carritoCompras.remove(producto)
                print("El producto hasido eliminado correctamente del carrito de compras.")
                return
        print("El producto no existe en el carrito de compras.")
        
    @classmethod
    def listarCarrito(cls):
        if cls.carritoCompras:
            print("Productos del carrito:")
            for producto in cls.carritoCompras:
                print("-----------------------")
                print("Código:", producto["Codigo"])
                print("Cantidad:", producto["Cantidad"])
                print("-----------------------")
                
        else:
            print("El carrito de compras está vacío.")
            
            
            
            