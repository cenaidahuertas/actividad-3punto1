from estadopedido import EstadoEnvio
from pedido import Pedido
from transportadora import EmpresaTransportadora

class Envio:
    def __init__(
        self, 
        pedido: Pedido, 
        empresa_transportadora: EmpresaTransportadora,
        estado: EstadoEnvio = EstadoEnvio.PENDIENTE
    ) -> None:
    
        self.pedido = pedido
        self.empresa_transportadora = empresa_transportadora
        self.estado = estado

    # ── pedido ───────────────────────────────────────────

    @property
    def pedido(self) -> Pedido:
        """Obtiene el pedido asociado al envío."""
        return self._pedido
    @pedido.setter
    def pedido(self, valor: Pedido) -> None:
        """Establece el pedido asociado al envío, asegurándose de que sea una instancia de Pedido."""
        if not isinstance(valor, Pedido):
            raise ValueError("El pedido debe ser una instancia de Pedido.")
        self._pedido = valor
 
    # ── empresa_transportadora ───────────────────────────────────

    @property
    def empresa_transportadora(self) -> EmpresaTransportadora:
        """Obtiene la empresa transportadora asociada al envío."""
        return self._empresa_transportadora
    @empresa_transportadora.setter
    def empresa_transportadora(self, valor: EmpresaTransportadora) -> None:
        """Establece la empresa transportadora asociada al envío, asegurándose de que sea una instancia de EmpresaTransportadora."""
        if not isinstance(valor, EmpresaTransportadora):
            raise ValueError("La empresa transportadora debe ser una instancia de EmpresaTransportadora.")
        self._empresa_transportadora = valor

    # ── estado ───────────────────────────────────

    @property
    def estado(self) -> EstadoEnvio:
        """Obtiene el estado del envío."""
        return self._estado
    @estado.setter
    def estado(self, valor: EstadoEnvio) -> None:
        """Establece el estado del envío, asegurándose de que sea una instancia de EstadoEnvio."""
        if not isinstance(valor, EstadoEnvio):
            raise ValueError("El estado del envío debe ser una instancia de EstadoEnvio.")
        self._estado = valor

  # ── métodos ───────────────────────────────    

    def despachar(self) -> bool:
        """Despacha el envío, cambiando su estado a DESPACHADO si está pendiente."""
        if self.estado == EstadoEnvio.PENDIENTE:
            self.estado = EstadoEnvio.DESPACHADO
            return True
        return False

    def entregar(self) -> bool:
        """Entrega el envío, cambiando su estado a ENTREGADO si está despachado."""
        if self.estado == EstadoEnvio.DESPACHADO:
            self.estado = EstadoEnvio.ENTREGADO
            return True
        return False

    # ── representación ───────────────────────────────────

    def __repr__(self) -> str:
        return (
            f"Envio(pedido={self._pedido!r}, "
            f"empresa_transportadora={self._empresa_transportadora!r}, "
            f"estado={self._estado!r})"
        )

    def __str__(self) -> str:
        return (
            f"Envío del Pedido ID: {self._pedido.id_pedido}\n"
            f"Empresa Transportadora: {self._empresa_transportadora.nombre}\n"
            f"Estado del Envío: {self._estado.value}"
        )
         