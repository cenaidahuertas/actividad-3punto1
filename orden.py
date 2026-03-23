class Pedido:
    def __init__(self, id_pedido, cliente):
        self.id = id_pedido
        self.productos = []
        self.total = 0
        self.estado = "PENDIENTE"
        self.cliente = cliente
