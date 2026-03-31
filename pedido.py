from datetime import date
from cliente import Cliente
from estadopedido import estadopedido


class Pedido:
    def __init__(
            self, 
            id_pedido: str, 
            cliente: Cliente,
            total: float,
            estado: estadopedido = estadopedido.PENDIENTE,
            fecha: date = None
    ) -> None:
      
        self.id_pedido = id_pedido
        self.cliente = cliente
        self.total = total
        self.estado = estado
        self.fecha = fecha if fecha is not None else date.today()   
    
    # ── id ───────────────────────────────────

    @property
    def id_pedido(self) -> str:
        """Obtiene el ID del pedido."""
        return self._id_pedido
    
    @id_pedido.setter
    def id_pedido(self, valor: str) -> None:
        """Establece el ID del pedido, asegurándose de que no esté vacío."""
        valor = valor.strip()
        if not valor:
            raise ValueError("El ID del pedido no puede estar vacío.")
        self._id_pedido = valor
    
    # ── cliente ───────────────────────────────────

    @property
    def cliente(self) -> Cliente:
        """Obtiene el cliente asociado al pedido."""
        return self._cliente
    
    @cliente.setter
    def cliente(self, valor: Cliente) -> None:
        """Establece el cliente asociado al pedido, asegurándose de que sea una instancia de Cliente."""
        if not isinstance(valor, Cliente):
            raise ValueError("El cliente debe ser una instancia de Cliente.")
        self._cliente = valor
    
    # ── total ───────────────────────────────────

    @property
    def total(self) -> float:
        """Obtiene el total del pedido."""
        return self._total
    
    @total.setter
    def total(self, valor: float) -> None:
        """Establece el total del pedido, asegurándose de que sea un número no negativo."""
        if not isinstance(valor, (int, float)) or valor < 0:
            raise ValueError("El total del pedido debe ser un número no negativo.")
        self._total = float(valor)
    
    # ── estado ───────────────────────────────────
    
    @property
    def estado(self) -> estadopedido:
        """Obtiene el estado del pedido."""
        return self._estado
    
    @estado.setter
    def estado(self, valor: estadopedido) -> None:
        """Establece el estado del pedido, asegurándose de que sea un valor válido de estadopedido."""
        if not isinstance(valor, estadopedido):
            raise ValueError("El estado del pedido debe ser una instancia de estadopedido.")
        self._estado = valor
    
    # ── fecha ───────────────────────────────────

    @property
    def fecha(self) -> date:
        """Obtiene la fecha del pedido."""
        return self._fecha
    
    @fecha.setter
    def fecha(self, valor: date) -> None:
        """Establece la fecha del pedido, asegurándose de que sea una instancia de date."""
        if not isinstance(valor, date):
            raise ValueError("La fecha del pedido debe ser una instancia de date.")
        self._fecha = valor

    # ── métodos ───────────────────────────────

    def cambiar_estado(self, nuevo_estado: estadopedido) -> None:
        """Cambia el estado del pedido a un nuevo estado válido."""
        if not isinstance(nuevo_estado, estadopedido):
            raise ValueError("El nuevo estado debe ser una instancia de estadopedido.")
        self._estado = nuevo_estado

    def cancelar (self) -> bool:
        """Cancela el pedido si no ha sido enviado; devuelve True si se canceló, False si no se pudo cancelar."""
        if self._estado in [estadopedido.PENDIENTE, estadopedido.CONFIRMADO]:
            self._estado = estadopedido.CANCELADO
            return True
        return False


    # ── representación ───────────────────────────────────

    def __repr__(self) -> str:
        return (
            f"Pedido(id_pedido={self._id_pedido!r}, "
            f"cliente={self._cliente!r}, "
            f"total={self._total!r}, "
            f"estado={self._estado!r}, "
            f"fecha={self._fecha!r})"
        )

    def __str__(self) -> str:
        return (
            f"Pedido ID: {self._id_pedido}\n"
            f"Cliente: {self._cliente.nombre}\n"
            f"Total: ${self._total:.2f}\n"
            f"Estado: {self._estado.value}\n"
    f"Fecha: {self._fecha.strftime('%Y-%m-%d')}"
)
    
