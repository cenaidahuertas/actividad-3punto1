import sys
import os
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class Queja:
    def __init__(
        self, 
        id: str,
        cliente: str,
        descripcion: str,
        estado: str = "REGISTRADA"
        )-> None:

        self.id = id
        self.cliente = cliente
        self.descripcion = descripcion
        self.estado = "REGISTRADA"


    @property
    def id(self) -> str:
        """Obtiene el ID de la queja."""
        return self._id
    @id.setter
    def id(self, valor: str) -> None:
        """Establece el ID de la queja."""
        self._id = valor

    @property
    def cliente(self) -> str:
        """Obtiene el cliente que presentó la queja."""
        return self._cliente
    @cliente.setter
    def cliente(self, valor: str) -> None:
        """Establece el cliente que presentó la queja."""
        self._cliente = valor

    @property
    def descripcion(self) -> str:
        """Obtiene la descripción de la queja."""
        return self._descripcion
    @descripcion.setter
    def descripcion(self, valor: str) -> None:
        """Establece la descripción de la queja."""
        self._descripcion = valor

    @property
    def estado(self) -> str:
        """Obtiene el estado de la queja."""
        return self._estado
    @estado.setter
    def estado(self, valor: str) -> None:
        """Establece el estado de la queja."""
        self._estado = valor

    def __repr__(self) -> str:
        return (
            f"Queja ID    : {self._id}\n"
            f"Cliente     : {self._cliente}\n"
            f"Descripción : {self._descripcion}\n"
            f"Estado      : {self._estado}"
        ) 
    
    def registrar_queja(self):
        """Permite al cliente presentar una queja o reclamo sobre un pedido o producto."""
        print(f"Queja registrada por {self.cliente}: {self.descripcion}")
    
    
# Ejemplo de uso------------------------------------------------------
if __name__ == "__main__":

    descripcion = input("Ingrese la descripción de su queja: ")
    if descripcion:
        try:
            queja1 = Queja(id="Q001", cliente="Juan Pérez", descripcion=descripcion)
            queja1.registrar_queja()
            print(queja1)
        except ValueError as e:
            print(f"Error al registrar la queja: {e}")
    else:
        print("La descripción de la queja no puede estar vacía.")
        