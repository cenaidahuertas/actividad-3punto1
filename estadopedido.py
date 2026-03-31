from enum import Enum

class EstadoPedido(Enum):
    PENDIENTE  = "PENDIENTE"
    CONFIRMADO = "CONFIRMADO"
    ENVIADO    = "ENVIADO"
    ENTREGADO  = "ENTREGADO"
    CANCELADO  = "CANCELADO"
    