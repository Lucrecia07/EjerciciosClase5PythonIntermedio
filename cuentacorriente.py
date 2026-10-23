from cuentabancaria import CuentaBancaria

# Definición de la clase CuentaCorriente que hereda de la clase padre CuentaBancaria.
class CuentaCorriente(CuentaBancaria):

    # Definición de la función de inicialización.
    def __init__(self, titular, cbu, saldo_inicial, limite_descubierto = 500):
        """
        Esta función inicializa los atributos, que hereda de la clase padre CuentaBancaria,
        y los atributos propios.
        Tiene cinco parámetros.
        """
        # Inicialización de los atributos que hereda de la clase padre CuentaBancaria.
        super().__init__(titular, cbu, saldo_inicial)
        # Inicialización del atributo de la propia clase.
        self._limite_descubierto = limite_descubierto

    # Definición de la funcion getter para leer el atributo protegido _limite_descubierto.
    @property
    def limite_descubierto(self):
        """
        Función getter del atributo protegido _limite_descubierto.
        Tiene un parámetro.
        Retorna el limite_descubierto.
        """
        return self._limite_descubierto

    # Definición de la función saldo, para sobreescribir el setter de la clase padre CuentaBancaria.
    # Para permitir el saldo negativo.
    @CuentaBancaria.saldo.setter
    def saldo(self, p_saldo):
        """
        Función setter del atributo saldo de la clase padre CuentaBancaria.
        Tiene dos parámetros.
        Permite saldo negativo hasta el límite descubierto.
        """
        if p_saldo < -(self._limite_descubierto):
            raise ValueError("El saldo contable no puede exceder al límite descubierto.")
        self._saldo = p_saldo

    # Definición de la función para extraer monto.
    def extraer(self, monto):
        """
        Esta función implementa la función abstracta de la clase padre CuentaBancaria.
        """ 
        # Permite extraer hasta agotar el saldo + descubierto.
        if monto > self.saldo + self._limite_descubierto:
            print(f"El monto que desea retirar: ${monto}, supera el saldo + limite descubierto: ${self.saldo + self.limite_descubierto}")
        else:
            # Utiliza el setter de la clase hija.
            self.saldo -= monto
            print(f"Extracción de ${monto} realizada. Saldo: ${self.saldo} (Límite desc: ${self.limite_descubierto}) ")