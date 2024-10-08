class Asignatura:
    def __init__(self, nombre: str, codigo: str, creditos: int):
        self._nombre = nombre
        self._codigo = codigo
        self._creditos = creditos

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        self._codigo = valor

    @property
    def creditos(self):
        return self._creditos

    @creditos.setter
    def creditos(self, valor):
        self._creditos = valor

    def mostrar_informacion(self):
        print(f"Asignatura: {self._nombre}, Código: {self._codigo}, Créditos: {self._creditos}")
