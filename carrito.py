class Carrito:
    def __init__(self,productos):
        self.productos = productos
        self.total = 0

    def agregar_producto(self, producto, cantidad):
        if cantidad <= 0 or producto.cantidad_disponible < cantidad:
            return False

        for i in range(cantidad):
            self.productos.append(producto)

        producto.cantidad_disponible = producto.cantidad_disponible - cantidad
        self.calcular_total()
        return True

    def calcular_total(self):
        self.total = 0
        for producto in self.productos:
            self.total = self.total + producto.precio
        return self.total
