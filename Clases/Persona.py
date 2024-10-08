class Persona:
    def __init__(self, nombre: str, apellido: str, fecha_de_nacimiento: str):
        self._nombre = nombre
        self._apellido = apellido
        self._fecha_de_nacimiento = fecha_de_nacimiento

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
    def fecha_de_nacimiento(self):
        return self._fecha_de_nacimiento

    @fecha_de_nacimiento.setter
    def fecha_de_nacimiento(self, valor):
        self._fecha_de_nacimiento = valor

    def presentarse(self):
        print(f"Hola, soy {self._nombre} {self._apellido}.")
