from Clases.estudiante import Estudiante
from Clases.profesor import Profesor
from Clases.asignatura import Asignatura
from Clases.grupo import Grupo
from Clases.ProgramaAcademico import ProgramaAcademico
from interfaz_GUI.app import App  # Importa la clase App

# Inicializar listas para almacenar entidades
estudiantes = []
profesores = []
asignaturas = []
grupos = []
programas_academicos = []

# Funciones de creación de entidades
def crear_grupo(nombre_asignatura, codigo_asignatura, nombre_profesor, departamento):
    asignatura = Asignatura(nombre_asignatura, codigo_asignatura, 4)
    profesor = Profesor(nombre_profesor, "Apellido", "FechaX", "12345", departamento)
    grupo = Grupo(1, asignatura, profesor)
    grupos.append(grupo)
    return grupo

def agregar_estudiante_a_grupo(grupo, nombre, apellido, matricula, carrera, semestre):
    estudiante = Estudiante(nombre, apellido, "FechaX", matricula, carrera, semestre)
    grupo.agregar_estudiante(estudiante)

def eliminar_estudiante_de_grupo(grupo, matricula):
    grupo.eliminar_estudiante(matricula)

def mostrar_info_grupo(grupo):
    grupo.mostrar_grupo()

# Agregar estudiante a la lista general
def agregar_estudiante(nombre, apellido, fecha_de_nacimiento, matricula, carrera, semestre):
    estudiante = Estudiante(nombre, apellido, fecha_de_nacimiento, matricula, carrera, semestre)
    estudiantes.append(estudiante)
    print(f"Estudiante agregado: {estudiante}")

# Agregar profesor
def agregar_profesor(nombre, apellido, fecha_de_nacimiento, numero_empleado, departamento):
    profesor = Profesor(nombre, apellido, fecha_de_nacimiento, numero_empleado, departamento)
    profesores.append(profesor)
    print(f"Profesor agregado: {profesor}")

# Agregar asignatura
def agregar_asignatura(nombre, codigo, creditos):
    asignatura = Asignatura(nombre, codigo, creditos)
    asignaturas.append(asignatura)
    print(f"Asignatura agregada: {asignatura}")

# Agregar grupo
def agregar_grupo(numero_grupo, asignatura, profesor):
    grupo = Grupo(numero_grupo, asignatura, profesor)
    grupos.append(grupo)
    print(f"Grupo agregado: {grupo}")

# Agregar programa académico
def agregar_programa_academico(nombre, codigo):
    programa = ProgramaAcademico(nombre, codigo)
    programas_academicos.append(programa)
    print(f"Programa Académico agregado: {programa}")

if __name__ == "__main__":
    app = App()
    app.mainloop()
