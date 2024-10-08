import tkinter as tk
from tkinter import messagebox
from main import agregar_estudiante_a_grupo, crear_grupo

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema Universitario")
        self.geometry("400x300")

        # Variables para almacenar los datos del formulario
        self.nombre = tk.StringVar()
        self.apellido = tk.StringVar()
        self.fecha_nacimiento = tk.StringVar()
        self.matricula = tk.StringVar()
        self.carrera = tk.StringVar()
        self.semestre = tk.IntVar()

        # Crea los widgets de la interfaz
        self.create_widgets()

    def create_widgets(self):
        # Etiquetas y entradas de texto
        tk.Label(self, text="Nombre:").pack()
        tk.Entry(self, textvariable=self.nombre).pack()

        tk.Label(self, text="Apellido:").pack()
        tk.Entry(self, textvariable=self.apellido).pack()

        tk.Label(self, text="Fecha de Nacimiento:").pack()
        tk.Entry(self, textvariable=self.fecha_nacimiento).pack()

        tk.Label(self, text="Matrícula:").pack()
        tk.Entry(self, textvariable=self.matricula).pack()

        tk.Label(self, text="Carrera:").pack()
        tk.Entry(self, textvariable=self.carrera).pack()

        tk.Label(self, text="Semestre:").pack()
        tk.Entry(self, textvariable=self.semestre).pack()

        # Botón para agregar estudiante
        self.btn_add_student = tk.Button(self, text="Agregar Estudiante", command=self.agregar_estudiante_grupo)
        self.btn_add_student.pack(pady=10)

    def agregar_estudiante_grupo(self):
        # Obtiene los datos del formulario
        nombre = self.nombre.get()
        apellido = self.apellido.get()
        fecha_nacimiento = self.fecha_nacimiento.get()
        matricula = self.matricula.get()
        carrera = self.carrera.get()
        semestre = self.semestre.get()

        # Lógica para agregar el estudiante al grupo usando las funciones del main.py
        try:
            grupo_actual = crear_grupo("Matemáticas", "MAT101", "Profesor X", "Ciencias")
            agregar_estudiante_a_grupo(grupo_actual, nombre, apellido, matricula, carrera, semestre)
            messagebox.showinfo("Éxito", f"Estudiante {nombre} {apellido} agregado al grupo.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al agregar estudiante: {str(e)}")

if __name__ == "__main__":
    app = App()
    app.mainloop()
