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

    # ── métodos ───────────────────────────────
    
    def agregar_producto(self, producto: "Producto", cantidad: int ) -> bool:
        """Agrega un producto al carrito, verificando que la cantidad sea positiva."""
        if not isinstance(producto, Producto):
            raise ValueError("El producto debe ser una instancia de Producto.")
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad debe ser un entero positivo.")
        
        for _ in range(cantidad):
            self._productos_seleccionados.append(producto)
        
        self.calcular_total()  # Recalcula el total después de agregar el producto
        return True
    
    def eliminar_producto(self, producto: "Producto", cantidad: int) -> bool:
        """Elimina un producto del carrito, verificando que la cantidad sea positiva y que el producto exista en el carrito."""
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
                break  # Si el producto no está más en el carrito, salimos del ciclo
        
        self.calcular_total()  # Recalcula el total después de eliminar el producto
        return eliminados > 0
    
    def calcular_total(self) -> None:
        """Calcula el total del carrito sumando los precios de los productos seleccionados."""
        self._total = sum(producto.precio for producto in self._productos_seleccionados)

    def confimar_pedido(self) -> str:
        """Confirma el pedido, devolviendo un mensaje con el total a pagar."""
        if not self._productos_seleccionados:
            return "El carrito está vacío. No se puede confirmar el pedido."
        return f"Pedido confirmado. Total a pagar: ${self._total:.2f}"
    
    # ── representación ───────────────────────────────────
    def __repr__(self) -> str:
        return (
            f"Carrito(productos_seleccionados={self._productos_seleccionados!r}, "
            f"total={self._total!r})"
        )   
    def __str__(self) -> str:
        productos_str = "\n".join(
            f"- {producto.nombre} (${producto.precio:.2f})"
            for producto in self._productos_seleccionados
        )
        return (
            f"Productos seleccionados:\n{productos_str}\n"
            f"Total: ${self._total:.2f}"
        )
    
    