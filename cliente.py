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

    def p
        