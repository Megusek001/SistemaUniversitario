import customtkinter as ctk
from tkinter import messagebox
from Clases.Estudiante import Estudiante
from Clases.Profesor import Profesor
from Clases.Asignatura import Asignatura
from Clases.Grupo import Grupo
from Clases.ProgramaAcademico import ProgramaAcademico

class Interfaz:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema Universitario")
        self.master.geometry("800x800")
        ctk.set_appearance_mode("System")  # Modo oscuro o claro
        ctk.set_default_color_theme("blue")  # Cambiar el tema a azul
        self.programa_academico = ProgramaAcademico("Ingeniería en Sistemas", "IS123")

        # Frame para la gestión de estudiantes
        self.frame_estudiante = ctk.CTkFrame(master)
        self.frame_estudiante.pack(pady=20, padx=20, fill="both", expand=True)

        ctk.CTkLabel(self.frame_estudiante, text="Gestionar Estudiantes", font=("Arial", 16)).grid(row=0, columnspan=2, pady=10)

        ctk.CTkLabel(self.frame_estudiante, text="Nombre:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_nombre_estudiante = ctk.CTkEntry(self.frame_estudiante)
        self.entry_nombre_estudiante.grid(row=1, column=1, padx=10, pady=5)

        ctk.CTkLabel(self.frame_estudiante, text="Apellido:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_apellido_estudiante = ctk.CTkEntry(self.frame_estudiante)
        self.entry_apellido_estudiante.grid(row=2, column=1, padx=10, pady=5)

        ctk.CTkLabel(self.frame_estudiante, text="Matrícula:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.entry_matricula_estudiante = ctk.CTkEntry(self.frame_estudiante)
        self.entry_matricula_estudiante.grid(row=3, column=1, padx=10, pady=5)

        ctk.CTkButton(self.frame_estudiante, text="Agregar Estudiante", command=self.agregar_estudiante).grid(row=4, columnspan=2, pady=10)

        # Frame para la gestión de grupos
        self.frame_grupo = ctk.CTkFrame(master)
        self.frame_grupo.pack(pady=20, padx=20, fill="both", expand=True)

        ctk.CTkLabel(self.frame_grupo, text="Gestionar Grupos", font=("Arial", 16)).grid(row=0, columnspan=2, pady=10)

        ctk.CTkLabel(self.frame_grupo, text="Número de Grupo:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_numero_grupo = ctk.CTkEntry(self.frame_grupo)
        self.entry_numero_grupo.grid(row=1, column=1, padx=10, pady=5)

        ctk.CTkButton(self.frame_grupo, text="Agregar Grupo", command=self.agregar_grupo).grid(row=2, columnspan=2, pady=10)

        # Frame para inscribir estudiantes a grupos
        self.frame_inscripcion = ctk.CTkFrame(master)
        self.frame_inscripcion.pack(pady=20, padx=20, fill="both", expand=True)

        ctk.CTkLabel(self.frame_inscripcion, text="Inscripción de Estudiantes", font=("Arial", 16)).grid(row=0, columnspan=2, pady=10)

        ctk.CTkLabel(self.frame_inscripcion, text="Matrícula Estudiante:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_matricula_inscripcion = ctk.CTkEntry(self.frame_inscripcion)
        self.entry_matricula_inscripcion.grid(row=1, column=1, padx=10, pady=5)

        ctk.CTkLabel(self.frame_inscripcion, text="Número de Grupo:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_numero_grupo_inscripcion = ctk.CTkEntry(self.frame_inscripcion)
        self.entry_numero_grupo_inscripcion.grid(row=2, column=1, padx=10, pady=5)

        ctk.CTkButton(self.frame_inscripcion, text="Inscribir Estudiante", command=self.inscribir_estudiante).grid(row=3, columnspan=2, pady=10)

        # Frame para mostrar información
        self.frame_info = ctk.CTkFrame(master)
        self.frame_info.pack(pady=20, padx=20, fill="both", expand=True)

        ctk.CTkButton(self.frame_info, text="Mostrar Grupos", command=self.mostrar_grupos).grid(row=0, column=0, pady=10)

    def agregar_estudiante(self):
        nombre = self.entry_nombre_estudiante.get()
        apellido = self.entry_apellido_estudiante.get()
        matricula = self.entry_matricula_estudiante.get()

        if not nombre or not apellido or not matricula:
            messagebox.showerror("Error", "Por favor, completa todos los campos.")
            return

        estudiante = Estudiante(nombre, apellido, "2000-01-01", matricula, "Ingeniería en Sistemas", 1)
        self.programa_academico.agregar_grupo(Grupo(1, Asignatura("Programación", "PROG101", 4), Profesor("Juan", "Pérez", "1980-01-01", "12345", "Computación")))
        grupo = self.programa_academico._grupos[0]  # Obtener el primer grupo

        grupo.agregar_estudiante(estudiante)
        messagebox.showinfo("Éxito", f"Estudiante {nombre} {apellido} agregado.")

    def agregar_grupo(self):
        numero_grupo = self.entry_numero_grupo.get()

        if not numero_grupo:
            messagebox.showerror("Error", "Por favor, completa el campo del número de grupo.")
            return

        grupo = Grupo(int(numero_grupo), Asignatura("Programación", "PROG101", 4), Profesor("Juan", "Pérez", "1980-01-01", "12345", "Computación"))
        self.programa_academico.agregar_grupo(grupo)
        messagebox.showinfo("Éxito", f"Grupo {numero_grupo} agregado.")

    def inscribir_estudiante(self):
        matricula = self.entry_matricula_inscripcion.get()
        numero_grupo = self.entry_numero_grupo_inscripcion.get()

        if not matricula or not numero_grupo:
            messagebox.showerror("Error", "Por favor, completa todos los campos.")
            return

        grupo_encontrado = None
        for grupo in self.programa_academico._grupos:
            if grupo.numero_grupo == int(numero_grupo):
                grupo_encontrado = grupo
                break

        if grupo_encontrado:
            for estudiante in grupo_encontrado._estudiantes:
                if estudiante.matricula == matricula:
                    messagebox.showinfo("Éxito", f"Estudiante con matrícula {matricula} ya está en el grupo.")
                    return

            # Crear un nuevo estudiante si no se encuentra
            nuevo_estudiante = Estudiante("Nuevo", "Estudiante", "2000-01-01", matricula, "Ingeniería en Sistemas", 1)
            grupo_encontrado.agregar_estudiante(nuevo_estudiante)
            messagebox.showinfo("Éxito", f"Estudiante con matrícula {matricula} inscrito en el grupo {numero_grupo}.")
        else:
            messagebox.showerror("Error", "Número de grupo no encontrado.")

    def mostrar_grupos(self):
        grupos_info = ""
        for grupo in self.programa_academico._grupos:
            grupos_info += f"Grupo: {grupo.numero_grupo}, Asignatura: {grupo._asignatura.nombre}\n"

        if grupos_info:
            messagebox.showinfo("Grupos", grupos_info)
        else:
            messagebox.showinfo("Grupos", "No hay grupos registrados.")

# Ejemplo de inicialización de la interfaz
if __name__ == "__main__":
    root = ctk.CTk()
    app = Interfaz(root)
    root.mainloop()