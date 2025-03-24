from uuid import UUID, uuid4
from dataclasses import dataclass, field
from typing import Dict, List, Optional
from datetime import datetime
from programa_academico import ProgramaAcademico

@dataclass
class SolicitudAulas:
    programa: ProgramaAcademico
    fecha_solicitud: datetime = field(default_factory=datetime.now)
    estado: str = "pendiente"  # pendiente, aprobada, rechazada
    asignaciones: List[Dict] = field(default_factory=list)

    @classmethod
    def crear(cls, programa: ProgramaAcademico) -> 'SolicitudAulas':
        """Crea una nueva solicitud de aulas."""
        return cls(programa=programa)

    def serializar(self) -> Dict:
        """Convierte la solicitud a un diccionario para transmisión."""
        return {
            "programa_academico": {
                "id": str(self.programa.id),
                "nombre": self.programa.nombre,
                "semestre": self.programa.semestre,
                "salones_solicitados": self.programa.salones_solicitados,
                "laboratorios_solicitados": self.programa.laboratorios_solicitados
            },
            "fecha_solicitud": self.fecha_solicitud.isoformat(),
            "estado": self.estado,
            "asignaciones": self.asignaciones
        }

    @classmethod
    def deserializar(cls, data: Dict) -> 'SolicitudAulas':
        """Crea una solicitud a partir de un diccionario."""
        programa = ProgramaAcademico(
            id=UUID(data["programa_academico"]["id"]),
            nombre=data["programa_academico"]["nombre"],
            semestre=data["programa_academico"]["semestre"],
            salones_solicitados=data["programa_academico"]["salones_solicitados"],
            laboratorios_solicitados=data["programa_academico"]["laboratorios_solicitados"]
        )
        
        return cls(
            programa=programa,
            fecha_solicitud=datetime.fromisoformat(data["fecha_solicitud"]),
            estado=data["estado"],
            asignaciones=data["asignaciones"]
        )

    def actualizar_estado(self, nuevo_estado: str) -> None:
        """Actualiza el estado de la solicitud."""
        estados_validos = ["pendiente", "aprobada", "rechazada"]
        if nuevo_estado not in estados_validos:
            raise ValueError(f"Estado no válido. Debe ser uno de: {estados_validos}")
        self.estado = nuevo_estado

    def agregar_asignacion(self, asignacion: Dict) -> None:
        """Agrega una asignación a la solicitud."""
        self.asignaciones.append(asignacion)

    def __str__(self) -> str:
        return f"Solicitud de {self.programa.nombre} - Estado: {self.estado}"

    def __repr__(self) -> str:
        return f"SolicitudAulas(programa='{self.programa.nombre}', estado='{self.estado}')" 