class Producto:
    def __init__(
        self, 
        codigo: str, 
        nombre: str, 
        descripcion: str, 
        precio: float, 
        cantidad_disponible: int

    ) -> None:
        
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible

    @property
    def codigo(self) -> str:
        """Obtiene el código del producto."""
        return self._codigo

    @codigo.setter
    def codigo(self, valor: str) -> None:
        """Establece el código del producto, asegurándose de que no esté vacío."""
        valor = valor.strip()
        if not valor:
            raise ValueError("El código no puede estar vacío.")
        self._codigo = valor

    @property
    def nombre(self) -> str:
        """Obtiene el nombre del producto."""
        return self._nombre 
    @nombre.setter
    def nombre(self, valor: str) -> None:
        """Establece el nombre del producto, asegurándose de que no esté vacío."""
        valor = valor.strip()
        if not valor:
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = valor
    @property
    def descripcion(self) -> str:
        """Obtiene la descripción del producto."""
        return self._descripcion
    @descripcion.setter
    def descripcion(self, valor: str) -> None:
        """Establece la descripción del producto, asegurándose de que no esté vacía."""
        valor = valor.strip()
        if not valor:
            raise ValueError("La descripción no puede estar vacía.")
        self._descripcion = valor
    @property
    def precio(self) -> float:
        """Obtiene el precio del producto."""
        return self._precio
    @precio.setter
    def precio(self, valor: float) -> None:
        """Establece el precio del producto, asegurándose de que sea un número positivo."""
        if valor <= 0:
            raise ValueError("El precio debe ser un número positivo.")
        self._precio = valor
    @property
    def cantidad_disponible(self) -> int:
        """Obtiene la cantidad disponible del producto."""
        return self._cantidad_disponible
    @cantidad_disponible.setter
    def cantidad_disponible(self, valor: int) -> None:
        """Establece la cantidad disponible del producto, asegurándose de que sea un número entero no negativo."""
        if valor < 0:
            raise ValueError("La cantidad disponible no puede ser negativa.")
        self._cantidad_disponible = valor        