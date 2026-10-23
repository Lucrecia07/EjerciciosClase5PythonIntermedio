from abc import ABC, abstractmethod

# Definición de clase base abstracta CuentaBancaria.
class CuentaBancaria(ABC):

    # Definición de la función de inicialización.
    def __init__(self, titular, cbu, saldo):
        """
        Esta función inicializa los atributos de la clase.
        Tiene cuatro parámetros.
        """
        # Atributo público.
        self.titular = titular
        # Atributo protegido, de solo lectura mediante @property.
        self._cbu = cbu
        # Atributo protegido, con @property para leer y @saldo.setter para modificar.
        self._saldo = saldo

    # Definición de la función getter para leer el atributo protegido _cbu.
    @property
    def cbu(self):
        """
        Función getter del atributo protegido _cbu
        Tiene un parámetro.
        Retorna el cbu.
        """
        return self._cbu

    # Definición de la función getter para leer el atributo protegido _saldo.
    @property
    def saldo(self):
        """
        Función getter del atributo protegido _saldo.
        Tiene un parámetro.
        Retorna el saldo.
        """
        return self._saldo

    # Definición de la función setter para modificar el atributo protegido _saldo.
    @saldo.setter
    def saldo(self, p_saldo):
        """
        Función setter del atributo protegido _saldo.
        Tiene dos parámetros. Un parámetro es el nuevo valor de _saldo.
        Luego de la validación, se modifica el _saldo.
        """
        # Validación de p_saldo
        if p_saldo < 0:
            raise ValueError("El saldo contable no puede ser negativo.")
        self._saldo = p_saldo

    # Definición de la función para depositar monto.
    def depositar(self, monto):
        """
        Esta función deposita el monto ingresado, previa validación.
        Recibe dos parámetro.
        """
        if monto <= 0:
            raise ValueError("El monto deber ser mayor a cero.")
        self.saldo += monto

    # Definición de la función __str__
    def __str__(self):
        """
        Esta función muestra el estado de los atributos de la cuenta.
        Tiene un parámetro.
        Retorna información general de la cuenta.
        """
        return f"[{type(self).__name__}] {self.titular} (CBU: {self.cbu}) | Saldo: ${self.saldo:.2f}"

    # Definición de la función abstracta extraer.
    @abstractmethod
    def extraer(self, monto):
        """
        Esta función debe ser implementada por cada subclase.
        Cada cuenta implementará su propia regla de extracción.
        """
        pass