from Clases.ProgramaAcademico import ProgramaAcademico
from Clases.Profesor import Profesor
from Clases.Asignatura import Asignatura
from Clases.Grupo import Grupo
from Clases.Estudiante import Estudiante
from interfaz.interfazTkinter import Interfaz
import tkinter as tk

def main():
    # Crear instancias de las clases
    programa = ProgramaAcademico("Ingeniería en Sistemas", "IS123")
    profesor = Profesor("Juan", "Pérez", "1980-01-01", "12345", "Computación")
    asignatura = Asignatura("Programación", "PROG101", 4)
    grupo = Grupo(1, asignatura, profesor)

    # Crear estudiantes
    estudiante1 = Estudiante("Ana", "Gómez", "2000-05-10", "E001", "Ingeniería en Sistemas", 1)
    estudiante2 = Estudiante("Luis", "Martínez", "1999-07-20", "E002", "Ingeniería en Sistemas", 1)

    # Agregar estudiantes al grupo
    grupo.agregar_estudiante(estudiante1)
    grupo.agregar_estudiante(estudiante2)

    # Agregar grupo al programa académico
    programa.agregar_grupo(grupo)

    # Crear y mostrar la interfaz
    root = tk.Tk()
    app = Interfaz(root)
    root.mainloop()

if __name__ == "__main__":
    main()
