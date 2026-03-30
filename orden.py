class Pedido:
    def __init__(self, id_pedido, cliente, productos):
        self.id = id_pedido
        self.productos = productos
        self.total = sum(producto.precio * producto.cantidad for producto in productos)
        self.estado = "PENDIENTE"
        self.cliente = cliente
