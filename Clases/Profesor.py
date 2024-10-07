from Persona import Persona

class Profesor(Persona):
    _contador_profesores = 0

    def __init__(self, nombre: str, apellido: str, fecha_de_nacimiento: str, numero_empleado: str, departamento: str):
        super().__init__(nombre, apellido, fecha_de_nacimiento)
        self._numero_empleado = numero_empleado
        self._departamento = departamento
        Profesor._contador_profesores += 1

    @classmethod
    def cantidad_profesores(cls) -> int:
        return cls._contador_profesores

    def enseniar(self, materia: str) -> None:
        print(f"Profesor {self._nombre} está enseñando {materia}.")

    def presentarse(self) -> str:
        return super().presentarse() + f", Número Empleado: {self._numero_empleado}, Departamento: {self._departamento}"
