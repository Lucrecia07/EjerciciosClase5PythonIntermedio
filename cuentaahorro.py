from cuentabancaria import CuentaBancaria

# Definición de la clase CuentaAhorro que hereda de la clase padre CuentaBancaria.
class CuentaAhorro(CuentaBancaria):

    # Definición de la función de inicialización.
    def __init__(self, titular, cbu, saldo_inicial):
        """
        Esta función inicializa los atributos, que hereda de la clase padre CuentaBancaria,
        y de su propia clase.
        Tiene cuatro parámetros.
        """
        # Inicialización de los atributos que hereda de la clase padre CuentaBancaria.
        super().__init__(titular, cbu, saldo_inicial)
        # Inicialización del atributo de la propia clase.
        self.__tasa = 0.001

    # Definición de la función para aplicar interés.
    def aplicar_interes(self):
        """
        Esta función aplica interés con tasa fija.
        Tiene un parámetro.
        Aplica el interés según la tasa fija.
        """
        # tasa fija 0.1% -> 0.001
        interes = self.saldo * self.__tasa
        self.saldo = self.saldo + interes
        print(f"Interés mensual aplicado (${interes:.2f}). Nuevo saldo: ${self.saldo:.2f}")

    # Definición de la función para extraer monto.
    def extraer(self, monto): 
        """
        Esta función implementa la función abstracta de la clase padre CuentaBancaria.
        """
        if monto <= self.saldo:
            # Utilizar la función del padre @saldo.setter
            self.saldo = self.saldo - monto
            print(f"Extracción de {monto} completada. Saldo restante: ${self.saldo}")
        else:
            print(f"Saldo insuficiente. Usted desea extraer: ${monto} y su saldo es: ${self.saldo}")