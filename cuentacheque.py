from cuentabancaria import CuentaBancaria

# Definición de la clase CuentaCheque que hereda de la clase padre CuentaBancaria.
class CuentaCheque(CuentaBancaria):

    # Definición de la función de inicialización.
    def __init__(self, titular, cbu, saldo_inicial, costo_emision=50):
        """
        Esta función inicializa los atributos, que hereda de la clase padre CuentaBancaria.
        Tiene cinco parámetros.
        """
        super().__init__(titular, cbu, saldo_inicial)
        self._costo_emision = costo_emision

    # Definición de la función getter para leer el atributo protegido _costo_emision
    @property
    def costo_emision(self):
        """
        Función getter del atributo protegido _costo_emision
        Tiene un parámetro.
        Retorna el costo de emisión.
        """
        return self._costo_emision

    
    # Definición de la función para extraer monto.
    def extraer(self, monto):
        """
        Esta función implementa la función abstracta de la clase padre CuentaBancaria.
        """
        if self.saldo < monto + self.costo_emision:
            print(f"No tiene fondos suficiente para el monto que desea extraer.")
        else:
            self.saldo -= monto + self.costo_emision
            print(f"Cheque emitido por ${monto} (Comisión: ${self.costo_emision}). Saldo restante: ${self.saldo}")