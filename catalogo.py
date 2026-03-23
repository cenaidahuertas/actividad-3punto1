class Catalogo:
    def __init__(self, productos):
        self.productos = productos

    def buscar_producto(self, codigo):
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None
