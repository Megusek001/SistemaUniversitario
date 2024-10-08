from Clases.Grupo import Grupo

class ProgramaAcademico:
    def __init__(self, nombre, codigo):
        self._nombre = nombre
        self._codigo = codigo
        self._grupos = []

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        self._codigo = valor

    @property
    def grupos(self):
        return self._grupos  # Solo getter, no se puede establecer directamente.

    def agregar_grupo(self, grupo):
        if grupo in self._grupos:
            raise ValueError(f"El grupo {grupo.numero_grupo} ya está incluido en el programa.")
        self._grupos.append(grupo)

    def eliminar_grupo(self, numero_grupo):
        grupo_a_eliminar = next((g for g in self._grupos if g.numero_grupo == numero_grupo), None)
        if grupo_a_eliminar:
            self._grupos.remove(grupo_a_eliminar)
        else:
            raise ValueError(f"No se encontró un grupo con el número {numero_grupo}.")

    def mostrar_programa(self):
        grupos_info = "\n".join([f"Grupo {g.numero_grupo}: {g.asignatura.nombre}, Profesor: {g.profesor.nombre}" for g in self._grupos])
        return f"Programa Académico: {self._nombre}, Código: {self._codigo}\nGrupos:\n{grupos_info if grupos_info else 'No hay grupos registrados.'}"
