from dataclasses import dataclass, field
from typing import List
from programa_academico import ProgramaAcademico

@dataclass
class Facultad:
    nombre: str
    programas: List[ProgramaAcademico] = field(default_factory=list)

    def agregar_programa(self, programa: ProgramaAcademico) -> None:
        """Agrega un programa a la facultad."""
        self.programas.append(programa)

    def obtener_programa(self, nombre_programa: str) -> ProgramaAcademico:
        """Obtiene un programa por su nombre."""
        for programa in self.programas:
            if programa.nombre == nombre_programa:
                return programa
        raise ValueError(f"No se encontró el programa {nombre_programa}")

    def __str__(self) -> str:
        return f"{self.nombre} - {len(self.programas)} programas" 