class Persona:
    _contador_personas = 0

    def __init__(self, nombre: str, apellido: str, fecha_de_nacimiento: str):
        self._nombre = nombre
        self._apellido = apellido
        self._fecha_de_nacimiento = fecha_de_nacimiento
        Persona._contador_personas += 1

    @classmethod
    def cantidad_personas(cls) -> int:
        return cls._contador_personas

    def presentarse(self) -> str:
        return f"Nombre: {self._nombre} {self._apellido}, Fecha de Nacimiento: {self._fecha_de_nacimiento}"
