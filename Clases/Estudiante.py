from Clases.Persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre: str, apellido: str, fecha_de_nacimiento: str, matricula: str, carrera: str, semestre: int):
        super().__init__(nombre, apellido, fecha_de_nacimiento)
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

    def estudiar(self, materia: str, horas: int):
        print(f"El estudiante {self.nombre} ha estudiado {materia} durante {horas} horas.")

    def presentarse(self):
        print(f"Hola, soy {self.nombre} {self.apellido}, estudiante de {self.carrera}, cursando el semestre {self.semestre}.")
