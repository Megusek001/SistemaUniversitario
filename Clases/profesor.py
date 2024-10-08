from Clases.persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, apellido, fecha_nacimiento, numero_empleado, departamento):
        super().__init__(nombre, apellido, fecha_nacimiento)
        self._numero_empleado = numero_empleado
        self._departamento = departamento

    @property
    def numero_empleado(self):
        return self._numero_empleado

    @numero_empleado.setter
    def numero_empleado(self, valor):
        self._numero_empleado = valor

    @property
    def departamento(self):
        return self._departamento

    @departamento.setter
    def departamento(self, valor):
        self._departamento = valor

    def presentarse(self):
        return f"Soy {self._nombre} {self._apellido}, profesor del departamento de {self._departamento}."
