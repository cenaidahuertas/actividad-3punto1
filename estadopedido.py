from enum import Enum

class EstadoPedido(Enum):
    PENDIENTE  = "PENDIENTE"
    CONFIRMADO = "CONFIRMADO"
    ENVIADO    = "ENVIADO"
    ENTREGADO  = "ENTREGADO"
    CANCELADO  = "CANCELADO"
    DESPACHADO = "DESPACHADO"
    

class EstadoEnvio(Enum):
    PENDIENTE = "PENDIENTE"
    EN_RUTA   = "EN_RUTA"
    ENTREGADO = "ENTREGADO"
    DEVUELTO  = "DEVUELTO"
    