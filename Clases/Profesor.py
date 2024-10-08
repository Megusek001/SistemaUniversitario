from Clases.Profesor import Persona

class Profesor(Persona):
    def __init__(self, nombre: str, apellido: str, fecha_de_nacimiento: str, numero_empleado: str, departamento: str):
        super().__init__(nombre, apellido, fecha_de_nacimiento)
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

    def enseñar(self, materia: str):
        print(f"El profesor {self.nombre} está enseñando {materia}.")

    def presentarse(self):
        print(f"Hola, soy {self.nombre} {self.apellido}, profesor del departamento de {self.departamento}.")
