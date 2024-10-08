from Clases.Asignatura import Asignatura
from Clases.Profesor import Profesor

class Grupo:
    def __init__(self, numero_grupo, asignatura, profesor):
        self._numero_grupo = numero_grupo
        self._asignatura = asignatura
        self._profesor = profesor
        self._estudiantes = []

    @property
    def numero_grupo(self):
        return self._numero_grupo

    @numero_grupo.setter
    def numero_grupo(self, valor):
        self._numero_grupo = valor

    @property
    def asignatura(self):
        return self._asignatura

    @asignatura.setter
    def asignatura(self, valor):
        self._asignatura = valor

    @property
    def profesor(self):
        return self._profesor

    @profesor.setter
    def profesor(self, valor):
        self._profesor = valor

    @property
    def estudiantes(self):
        return self._estudiantes  # Solo getter, no se puede establecer directamente.

    def agregar_estudiante(self, estudiante):
        if estudiante in self._estudiantes:
            raise ValueError(f"El estudiante {estudiante.matricula} ya está inscrito en el grupo.")
        self._estudiantes.append(estudiante)

    def eliminar_estudiante(self, matricula):
        estudiante_a_eliminar = next((e for e in self._estudiantes if e.matricula == matricula), None)
        if estudiante_a_eliminar:
            self._estudiantes.remove(estudiante_a_eliminar)
        else:
            raise ValueError(f"No se encontró un estudiante con matrícula {matricula}.")

    def mostrar_grupo(self):
        estudiantes_info = "\n".join([f"{e.nombre} {e.apellido}, Matrícula: {e.matricula}" for e in self._estudiantes])
        return f"Grupo {self._numero_grupo} de {self._asignatura.nombre}, Profesor: {self._profesor.nombre}\nEstudiantes:\n{estudiantes_info if estudiantes_info else 'No hay estudiantes.'}"
