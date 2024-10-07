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
    def nombre(self, value):
        self._nombre = value

    def agregar_grupo(self, grupo):
        if grupo not in self._grupos:
            self._grupos.append(grupo)
            print(f"Grupo {grupo.numero_grupo} agregado al programa {self._nombre}.")
        else:
            print("El grupo ya está incluido en el programa.")

    def eliminar_grupo(self, numero_grupo):
        for grupo in self._grupos:
            if grupo.numero_grupo == numero_grupo:
                self._grupos.remove(grupo)
                print(f"Grupo {numero_grupo} eliminado del programa {self._nombre}.")
                return
        print("Número de grupo no encontrado en el programa.")

    def mostrar_programa(self):
        print(f"Programa Académico: {self._nombre}, Código: {self._codigo}")
        print("Grupos:")
        for grupo in self._grupos:
            print(f"- Grupo: {grupo.numero_grupo}")
