from Clases.Persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, apellido, fecha_nacimiento, matricula, carrera, semestre):
        super().__init__(nombre, apellido, fecha_nacimiento)
        self._matricula = matricula
        self._carrera = carrera
        self._semestre = semestre

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, valor):
        self._matricula = valor

    @property
    def carrera(self):
        return self._carrera

    @carrera.setter
    def carrera(self, valor):
        self._carrera = valor

    @property
    def semestre(self):
        return self._semestre

    @semestre.setter
    def semestre(self, valor):
        self._semestre = valor

    def presentarse(self):
        return f"Soy {self._nombre} {self._apellido}, estudiante de {self._carrera}, en el semestre {self._semestre}."
