class DispositivoEntrada():
    def __init__(self,marca,tipo_entrada):
        self._tipo_entrada = tipo_entrada
        self._marca = marca

    @property
    def tipoEntrada(self):
        return self._tipoEntrada

    @property
    def marca(self):
        return self._marca

    @tipoEntrada.setter
    def tipoEntrada(self,tipo_entrada):
        self._tipoEntrada = tipo_entrada

    @marca.setter
    def marca(self,marca):
        self._marca = marca

    def __str__(self):
        return f'Marca: {self._marca}, El tipo de entrada es: {self._tipo_entrada}'


