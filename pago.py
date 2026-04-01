from abc import abstractmethod


class Pago:
    def __init__(
        self, 
        numero:str,
        fecha_vencimiento:str, 
        cvv:str
        ) -> None:

        self.numero = numero
        self.fecha_vencimiento = fecha_vencimiento
        self.cvv = cvv

    # ── número de tarjeta ───────────────────────────────────

    @property
    def numero(self) -> str:
        """Obtiene el número de la tarjeta de crédito."""
        return self._numero
    @numero.setter
    def numero(self, valor: str) -> None:
        """Establece el número de la tarjeta de crédito, asegurándose de que tenga 16 dígitos."""
        valor = valor.replace(" ", "")  # Elimina espacios
        if not valor.isdigit() or len(valor) != 16:
            raise ValueError("El número de la tarjeta debe tener 16 dígitos.")
        self._numero = valor

    # ── fecha de vencimiento ───────────────────────────────────

    @property
    def fecha_vencimiento(self) -> str:
        """Obtiene la fecha de vencimiento de la tarjeta de crédito."""
        return self._fecha_vencimiento
    @fecha_vencimiento.setter
    def fecha_vencimiento(self, valor: str) -> None:
        """Establece la fecha de vencimiento de la tarjeta de crédito, asegurándose de que tenga el formato MM/AA."""
        valor = valor.strip()
        if len(valor) != 5 or valor[2] != "/":
            raise ValueError("La fecha de vencimiento debe tener el formato MM/AA.")
        mes, año = valor.split("/")
        if not (mes.isdigit() and año.isdigit()):
            raise ValueError("La fecha de vencimiento debe contener solo números y '/'.")
        if not (1 <= int(mes) <= 12):
            raise ValueError("El mes debe estar entre 01 y 12.")
        self._fecha_vencimiento = valor
    
    # ── CVV ───────────────────────────────────
    
    @property
    def cvv(self) -> str:
        """Obtiene el CVV de la tarjeta de crédito."""
        return self._cvv
    @cvv.setter
    def cvv(self, valor: str) -> None:
        """Establece el CVV de la tarjeta de crédito, asegurándose de que tenga 3 dígitos."""
        valor = valor.strip()
        if not valor.isdigit() or len(valor) != 3:
            raise ValueError("El CVV debe tener 3 dígitos.")
        self._cvv = valor

    # ── método abstracto ─────────────────────────────────
    @abstractmethod
    def procesar_pago(self, total: float) -> bool:
        """Procesa el pago; debe ser implementado por cada subclase."""
        pass

    # ── representaciones  ─────────────────────────────────

    def __repr__(self) -> str:
        return (
            f"Pago(numero={self._numero!r}, "
            f"fecha_vencimiento={self._fecha_vencimiento!r}, "
            f"cvv={'*' * len(self._cvv)})"
        )
    def __str__(self) -> str:
        return (
            f"Número de tarjeta: {'*' * 12 + self._numero[-4:]}\n"
            f"Fecha de vencimiento: {self._fecha_vencimiento}\n"
            f"CVV: {'*' * len(self._cvv)}"
        )
        
        
class PagoTarjeta(Pago):
    
    def procesar_pago(self, total: float) -> bool:
        """Procesa el pago verificando que el total sea positivo."""
        if not isinstance(total, (int, float)):
            raise TypeError("El total debe ser un número.")
        if total <= 0:
            raise ValueError("El total debe ser mayor a cero.")
        return True
    
    
