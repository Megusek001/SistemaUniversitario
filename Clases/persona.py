class Persona:
    def __init__(self, nombre, apellido, fecha_nacimiento):
        self._nombre = nombre
        self._apellido = apellido
        self._fecha_nacimiento = fecha_nacimiento

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, valor):
        self._apellido = valor

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, valor):
        self._fecha_nacimiento = valor

    def presentarse(self):
        return f"Soy {self._nombre} {self._apellido}, nacido el {self._fecha_nacimiento}."
