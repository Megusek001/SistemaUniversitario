class Asignatura:
    def __init__(self, nombre, codigo, creditos):
        self._nombre = nombre
        self._codigo = codigo
        self._creditos = creditos

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    def mostrar_informacion(self):
        print(f"Asignatura: {self._nombre}, Código: {self._codigo}, Créditos: {self._creditos}.")
