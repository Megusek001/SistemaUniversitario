from Clases.Persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, apellido, fecha_de_nacimiento, matricula, carrera, semestre):
        super().__init__(nombre, apellido, fecha_de_nacimiento)
        self._matricula = matricula
        self._carrera = carrera
        self._semestre = semestre

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, value):
        self._matricula = value

    def estudiar(self, materia, horas):
        print(f"{self._nombre} está estudiando {materia} durante {horas} horas.")

    def presentarse(self):
        super().presentarse()
        print(f"Soy estudiante de {self._carrera}, matrícula: {self._matricula}.")
