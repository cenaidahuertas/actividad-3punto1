from producto import Producto

class Carrito:
    def __init__(
        self,
        productos: list
    ) -> None:
        self.productos_seleccionados = productos if productos is not None else []
        self._total: float = 0.0
        self.calcular_total()

    # ── Productos seleccionados ──────────────────────────────────────────
    @property
    def productos_seleccionados(self) -> list:
        """Obtiene la lista de productos seleccionados."""
        return self._productos_seleccionados        

    @productos_seleccionados.setter
    def productos_seleccionados(self, valor: list) -> None:
       """Establece la lista de productos; debe ser una lista válida."""
       if not isinstance(valor, list):
          raise ValueError("Los productos seleccionados deben ser una lista.")
       self._productos_seleccionados = valor

    @property
    def total(self) -> float:
        """Obtiene el total del carrito."""
        return self._total
    
    def calcular_total(self) -> None:
        """Calcula el total del carrito sumando los precios de los productos seleccionados."""
        self._total = sum(producto.precio for producto in self._productos_seleccionados)

   # ── métodos ──────────────────────────────────────────
    def agregar_producto(self, producto: "Producto", cantidad: int) -> bool:
        """Agrega un producto al carrito verificando stock."""
        if not isinstance(producto, Producto):
            raise ValueError("El producto debe ser una instancia de Producto.")
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad debe ser un entero positivo.")
        if producto.cantidad_disponible < cantidad:
            return False

        for _ in range(cantidad):
            self._productos_seleccionados.append(producto)

        producto.cantidad_disponible -= cantidad
        self.calcular_total()
        return True

    def eliminar_producto(self, producto: "Producto", cantidad: int) -> bool:
        """Elimina un producto del carrito devolviendo el stock."""
        if not isinstance(producto, Producto):
            raise ValueError("El producto debe ser una instancia de Producto.")
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad debe ser un entero positivo.")

        eliminados = 0
        for _ in range(cantidad):
            if producto in self._productos_seleccionados:
                self._productos_seleccionados.remove(producto)
                eliminados += 1
            else:
                break

        producto.cantidad_disponible += eliminados
        self.calcular_total()
        return eliminados > 0

    def confirmar_pedido(self) -> bool:
        """Confirma el pedido; retorna False si el carrito está vacío."""
        if not self._productos_seleccionados:
            return False
        return True

    # ── representación ───────────────────────────────────
    def __repr__(self) -> str:
        return (
            f"Carrito(productos_seleccionados={self._productos_seleccionados!r}, "
            f"total={self._total!r})"
        )

    def __str__(self) -> str:
        if not self._productos_seleccionados:
            return "El carrito está vacío."
        productos_str = "\n".join(
            f"- {producto.nombre} (${producto.precio:.2f})"
            for producto in self._productos_seleccionados
        )
        return (
            f"Productos seleccionados:\n{productos_str}\n"
            f"Total: ${self._total:.2f}"
        )