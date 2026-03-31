from carrito import Carrito


def formatear_precio(precio: float) -> str:
    """Formatea un precio como moneda."""
    return f"${precio:.2f}"


class Cliente:

    def __init__(
        self,
        nombre: str,
        correo: str,
        direccion: str
    ) -> None:
        self.nombre = nombre        # Usa el setter
        self.correo = correo        # Usa el setter
        self.direccion = direccion  # Usa el setter

    # ── nombre ──────────────────────────────────────────
    @property
    def nombre(self) -> str:
        """Obtiene el nombre del cliente."""
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        """Establece el nombre del cliente, asegurándose de que no esté vacío."""
        valor = valor.strip()
        if not valor:
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = valor

    # ── correo ──────────────────────────────────────────
    @property
    def correo(self) -> str:
        """Obtiene el correo del cliente."""
        return self._correo

    @correo.setter
    def correo(self, valor: str) -> None:
        """Establece el correo del cliente, asegurándose de que tenga un formato válido."""
        valor = valor.strip().lower()
        if "@" not in valor or "." not in valor.split("@")[-1]:
            raise ValueError(f"Correo inválido: '{valor}'")
        self._correo = valor

    # ── direccion ────────────────────────────────────────
    @property
    def direccion(self) -> str:
        """Obtiene la dirección del cliente."""
        return self._direccion

    @direccion.setter
    def direccion(self, valor: str) -> None:
        """Establece la dirección del cliente, asegurándose de que no esté vacía."""

        valor = valor.strip()
        if not valor:
            raise ValueError("La dirección no puede estar vacía.")
        self._direccion = valor

    # ── representación ───────────────────────────────────
    def __repr__(self) -> str:
        return (
            f"Cliente(nombre={self._nombre!r}, "
            f"correo={self._correo!r}, "
            f"direccion={self._direccion!r})"
        )

    def __str__(self) -> str:
        return (
            f"Nombre  : {self._nombre}\n"
            f"Correo  : {self._correo}\n"
            f"Dirección: {self._direccion}"
        )
    
    # ── métodos-------------------------------------------------------

    def ver_catalogo(self, catalogo):
        print("CATALOGO DE PRODUCTOS")
        for producto in catalogo.productos:
            print(
                "Codigo:", producto.codigo,
                "| Nombre:", producto.nombre,
                "| Precio:", formatear_precio(producto.precio),
                "| Stock:", producto.cantidad_disponible
            )
            print("Descripcion:", producto.descripcion)

    def crear_carrito(self) -> Carrito:
        """Crea y retorna un carrito de compras vacío para el cliente."""
        return Carrito(productos=[])  
    
    def ver_pedido(self, carrito):
        print("\nPEDIDO DEL CLIENTE")
        if len(carrito.productos) == 0:
            print("No hay productos en el carrito.")
            return

        for producto in carrito.productos:
            print(
                "Codigo:", producto.codigo,
                "| Nombre:", producto.nombre,
                "| Precio:", formatear_precio(producto.precio)
            )
            print("Descripcion:", producto.descripcion)
    
    def presentar_queja(self, mensaje: str) -> str:
        """Registra y retorna una queja del cliente."""
        mensaje = mensaje.strip()
        if not mensaje:
            raise ValueError("La queja no puede estar vacía.")
        return (
            f"Queja registrada\n"
            f"Cliente : {self._nombre}\n"
            f"Correo  : {self._correo}\n"
            f"Mensaje : {mensaje}"
        )
    
  # ── representación ───────────────────────────────────
    def __repr__(self) -> str:
        return (
            f"Cliente(nombre={self.nombre!r}, "
            f"correo={self.correo!r}, "
            f"direccion={self.direccion!r})"
        )

    def __str__(self) -> str:
        return (
            f"Nombre   : {self.nombre}\n"
            f"Correo   : {self.correo}\n"
            f"Dirección: {self.direccion}"
        )
    