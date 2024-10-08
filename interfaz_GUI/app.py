import tkinter as tk
from tkinter import messagebox
from Clases.Estudiante import Estudiante
from Clases.Profesor import Profesor
from Clases.Asignatura import Asignatura
from Clases.Grupo import Grupo
from Clases.ProgramaAcademico import ProgramaAcademico

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema Universitario")
        self.geometry("400x300")

        # Aquí puedes agregar elementos de la interfaz, como botones y campos de texto
        self.create_widgets()

    def create_widgets(self):
        # Botón para agregar un estudiante
        self.btn_add_student = tk.Button(self, text="Agregar Estudiante", command=self.add_student)
        self.btn_add_student.pack(pady=10)

        # Aquí puedes agregar más botones para otras funcionalidades

    def add_student(self):
        # Esta función se ejecutará al hacer clic en el botón "Agregar Estudiante"
        nombre = "Juan"
        apellido = "Pérez"
        fecha_nacimiento = "2000-01-01"
        matricula = "123456"
        carrera = "Ingeniería"
        semestre = 1

        estudiante = Estudiante(nombre, apellido, fecha_nacimiento, matricula, carrera, semestre)
        # Aquí puedes hacer algo con el estudiante, como agregarlo a una lista
        messagebox.showinfo("Estudiante Agregado", str(estudiante))

if __name__ == "__main__":
    app = App()  # Esta línea se ejecuta solo si el archivo es ejecutado directamente
    app.mainloop()
