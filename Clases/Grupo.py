from Clases.Asignatura import Asignatura
from Clases.Profesor import Profesor
from Clases.Estudiante import Estudiante

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
    def numero_grupo(self, value):
        self._numero_grupo = value

    def agregar_estudiante(self, estudiante):
        if estudiante not in self._estudiantes:
            self._estudiantes.append(estudiante)
            print(f"Estudiante {estudiante.nombre} agregado al grupo {self._numero_grupo}.")
        else:
            print("El estudiante ya está inscrito en este grupo.")

    def eliminar_estudiante(self, matricula):
        for estudiante in self._estudiantes:
            if estudiante.matricula == matricula:
                self._estudiantes.remove(estudiante)
                print(f"Estudiante {estudiante.nombre} eliminado del grupo {self._numero_grupo}.")
                return
        print("Matrícula no encontrada en el grupo.")

    def mostrar_grupo(self):
        print(f"Grupo: {self._numero_grupo}, Asignatura: {self._asignatura.nombre}, Profesor: {self._profesor.nombre}")
        print("Estudiantes:")
        for estudiante in self._estudiantes:
            print(f"- {estudiante.nombre}")
