class Pago:
    def __init__(self, numero, fecha, cvv):
        self.numero = numero
        self.fecha = fecha
        self.cvv = cvv

    def validar_pago(self, total):
        if self.numero != "" and self.fecha != "" and self.cvv != "" and total > 0:
            return True
        return False
