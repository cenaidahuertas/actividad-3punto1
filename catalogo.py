from producto import Producto


class Catalogo:
    def __init__(
            self,
            productos: list[Producto] 
    | None = None
    ) -> None:
        self.productos = productos if productos is not None else []

# ── productos ────────────────────────────────────────
    @property
    def productos(self) -> list[Producto]:
        """Obtiene la lista de productos en el catálogo."""
        return self._productos
    @productos.setter
    def productos(self, valor: list[Producto]) -> None:
        """Establece la lista de productos en el catálogo, asegurándose de que sea una lista de instancias de Producto."""
        if not isinstance(valor, list):
            raise ValueError("Los productos deben ser una lista.")
        for item in valor:
            if not isinstance(item, Producto):
                raise ValueError("Todos los elementos de la lista deben ser instancias de Producto.")
        self._productos = valor

# ── métodos de negocio ───────────────────────────────

def buscar_producto(self, codigo: str) -> Producto | None:
        """Busca un producto en el catálogo por su código y lo devuelve; si no se encuentra, devuelve None."""
        for producto in self._productos:
            if producto.codigo == codigo:
                return producto
        return None

def filtrar(self, categoria: str) -> list[Producto]:
        """Filtra productos por categoría; retorna lista vacía si no hay coincidencias."""
        if not isinstance(categoria, str) or not categoria.strip():
            raise ValueError("La categoría debe ser una cadena no vacía.")
        return [p for p in self._productos if p.categoria == categoria]

# ── representación ───────────────────────────────────

def __repr__(self) -> str:
        return f"Catalogo(productos={self._productos!r})"
    
def __str__(self) -> str:
        if not self._productos:
            return "El catálogo está vacío."
        
        lineas = ["Catálogo de Productos:"]
        for producto in self._productos:
            lineas.append(f"- {producto.nombre} (Código: {producto.codigo}, Precio: ${producto.precio:.2f})")
        return "\n".join(lineas)


