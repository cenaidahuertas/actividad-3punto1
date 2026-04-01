from __future__ import annotations
from estadopedido import EstadoPedido as EstadoEnvio
from pedido import Pedido

class Transportadora:
    def __init__(
        self, 
        nombre: str, 
        costo_envio: float,
        tiempo_entrega: int
    ) -> None:
    
        self.nombre = nombre
        self.costo_envio = costo_envio
        self.tiempo_entrega = tiempo_entrega
        self.estado_envio = EstadoEnvio.PENDIENTE

    # ── nombre ───────────────────────────────────────────

    @property
    def nombre(self) -> str:    
        """Obtiene el nombre de la transportadora."""
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor: str) -> None:       
        """Establece el nombre de la transportadora, asegurándose de que no esté vacío."""
        valor = valor.strip()
        if not valor:
            raise ValueError("El nombre de la transportadora no puede estar vacío.")
        self._nombre = valor

    # ── costo_envio ───────────────────────────────────────

    @property
    def costo_envio(self) -> float: 
        """Obtiene el costo de envío."""
        return self._costo_envio
    
    @costo_envio.setter
    def costo_envio(self, valor: float) -> None:
        """Establece el costo de envío, asegurándose de que sea un número no negativo."""
        if not isinstance(valor, (int, float)) or valor < 0:
            raise ValueError("El costo de envío debe ser un número no negativo.")
        self._costo_envio = valor
    
    # ── tiempo_entrega ───────────────────────────────────
    @property
    def tiempo_entrega(self) -> int:
        """Obtiene el tiempo de entrega en días."""
        return self._tiempo_entrega
    
    @tiempo_entrega.setter
    def tiempo_entrega(self, valor: int) -> None:
        """Establece el tiempo de entrega en días, asegurándose de que sea un entero positivo."""
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("El tiempo de entrega debe ser un entero positivo.")
        self._tiempo_entrega = valor

    # ── estado_envio ───────────────────────────────────
    @property
    def estado_envio(self) -> EstadoEnvio:
        """Obtiene el estado del envío."""
        return self._estado_envio
    
    @estado_envio.setter
    def estado_envio(self, valor: EstadoEnvio) -> None:
        """Establece el estado del envío, asegurándose de que sea una instancia de EstadoEnvio."""
        if not isinstance(valor, EstadoEnvio):
            raise ValueError("El estado del envío debe ser una instancia de EstadoEnvio.")
        self._estado_envio = valor

    # ── métodos de la transportadora ───────────────────────────────

    def calcular_envio(self, pedido: Pedido) -> float:  
        """Calcula el costo total del envío sumando el costo de envío al total del pedido."""
        if not isinstance(pedido, Pedido):
            raise ValueError("El pedido debe ser una instancia de Pedido.")
        return pedido.total + self.costo_envio
    
    def despachar_pedido(self, pedido: Pedido) -> str:
        """Despacha un pedido, actualizando el estado del envío y devolviendo un mensaje de confirmación."""
        if not isinstance(pedido, Pedido):
            raise ValueError("El pedido debe ser una instancia de Pedido.")
        
        self.estado_envio = EstadoEnvio.ENVIADO
        return f"Pedido {pedido.id_pedido} despachado por {self.nombre}. Tiempo estimado de entrega: {self.tiempo_entrega} días."

    

    # ── representación ───────────────────────────────────
    
    def __repr__(self) -> str:
        return (
            f"Transportadora(nombre={self._nombre!r}, "
            f"costo_envio={self._costo_envio!r}, "
            f"tiempo_entrega={self._tiempo_entrega!r}, "
            f"estado_envio={self._estado_envio!r})"
        )
    
    def __str__(self) -> str:
        return (
            f"Transportadora: {self._nombre}\n"
            f"Costo de Envío: ${self._costo_envio:.2f}\n"
            f"Tiempo de Entrega: {self._tiempo_entrega} días\n"
            f"Estado del Envío: {self._estado_envio.value}"
        )
    