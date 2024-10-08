from Clases.Estudiante import Estudiante
from Clases.Profesor import Profesor
from Clases.Asignatura import Asignatura
from Clases.Grupo import Grupo
from Clases.ProgramaAcademico import ProgramaAcademico
from interfaz_GUI.app import App  # Importa la clase App
 
# Inicializar listas para almacenar entidades
estudiantes = []
profesores = []
asignaturas = []
grupos = []
programas_academicos = []

def agregar_estudiante(nombre, apellido, fecha_de_nacimiento, matricula, carrera, semestre):
    estudiante = Estudiante(nombre, apellido, fecha_de_nacimiento, matricula, carrera, semestre)
    estudiantes.append(estudiante)
    print(f"Estudiante agregado: {estudiante}")

def agregar_profesor(nombre, apellido, fecha_de_nacimiento, numero_empleado, departamento):
    profesor = Profesor(nombre, apellido, fecha_de_nacimiento, numero_empleado, departamento)
    profesores.append(profesor)
    print(f"Profesor agregado: {profesor}")

def agregar_asignatura(nombre, codigo, creditos):
    asignatura = Asignatura(nombre, codigo, creditos)
    asignaturas.append(asignatura)
    print(f"Asignatura agregada: {asignatura}")

def agregar_grupo(numero_grupo, asignatura, profesor):
    grupo = Grupo(numero_grupo, asignatura, profesor)
    grupos.append(grupo)
    print(f"Grupo agregado: {grupo}")

def agregar_programa_academico(nombre, codigo):
    programa = ProgramaAcademico(nombre, codigo)
    programas_academicos.append(programa)
    print(f"Programa Académico agregado: {programa}")

# Aquí puedes agregar más funciones para eliminar y mostrar, según sea necesario
if __name__ == "__main__":
    app = App()  # Crea una instancia de la clase App
    app.mainloop()  # Inicia el bucle de la interfaz gráfica
