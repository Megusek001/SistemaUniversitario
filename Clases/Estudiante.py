from Persona import Persona

class Estudiante(Persona):
    _contador_estudiantes = 0

    def __init__(self, nombre: str, apellido: str, fecha_de_nacimiento: str, matricula: str, carrera: str, semestre: int):
        super().__init__(nombre, apellido, fecha_de_nacimiento)
        self._matricula = matricula
        self._carrera = carrera
        self._semestre = semestre
        Estudiante._contador_estudiantes += 1

    @classmethod
    def cantidad_estudiantes(cls) -> int:
        return cls._contador_estudiantes

    def estudiar(self, materia: str, horas: int) -> None:
        print(f"Estudiante {self._nombre} está estudiando {materia} durante {horas} horas.")

    def presentarse(self) -> str:
        return super().presentarse() + f", Matrícula: {self._matricula}, Carrera: {self._carrera}, Semestre: {self._semestre}"
