from Clases.Persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, apellido, fecha_de_nacimiento, numero_empleado, departamento):
        super().__init__(nombre, apellido, fecha_de_nacimiento)
        self._numero_empleado = numero_empleado
        self._departamento = departamento

    @property
    def numero_empleado(self):
        return self._numero_empleado

    @numero_empleado.setter
    def numero_empleado(self, value):
        self._numero_empleado = value

    def enseñar(self, materia):
        print(f"{self._nombre} está enseñando {materia}.")

    def presentarse(self):
        super().presentarse()
        print(f"Soy profesor del departamento de {self._departamento}, número de empleado: {self._numero_empleado}.")
