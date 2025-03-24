from uuid import UUID, uuid4
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class ProgramaAcademico:
    nombre: str
    facultad: str
    id: UUID = field(default_factory=uuid4)
    salones_solicitados: int = 0
    laboratorios_solicitados: int = 0

    def generar_solicitud(self, salones: int, laboratorios: int) -> 'SolicitudAulas':
        """Genera una solicitud de aulas para el programa."""
        from solicitud_aulas import SolicitudAulas
        self.salones_solicitados = salones
        self.laboratorios_solicitados = laboratorios
        return SolicitudAulas.crear(self)

    def __str__(self) -> str:
        return f"{self.nombre} ({self.facultad})"

    def __repr__(self) -> str:
        return f"ProgramaAcademico(nombre='{self.nombre}', facultad='{self.facultad}')" 