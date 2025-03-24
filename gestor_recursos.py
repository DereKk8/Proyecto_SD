from dataclasses import dataclass, field
from typing import Dict, List, Optional
from threading import Lock
from solicitud_aulas import SolicitudAulas

@dataclass
class GestorRecursos:
    salones_disponibles: int = 380
    laboratorios_disponibles: int = 60
    asignaciones: List[Dict] = field(default_factory=list)
    _lock: Lock = field(default_factory=Lock)

    def verificar_disponibilidad(self, salones_necesarios: int, laboratorios_necesarios: int) -> bool:
        """Verifica si hay suficientes recursos disponibles."""
        with self._lock:
            return (self.salones_disponibles >= salones_necesarios and 
                   self.laboratorios_disponibles >= laboratorios_necesarios)

    def asignar_aulas(self, solicitud: SolicitudAulas) -> bool:
        """Asigna aulas a una solicitud si hay disponibilidad."""
        with self._lock:
            if not self.verificar_disponibilidad(
                solicitud.programa_academico.salones_solicitados,
                solicitud.programa_academico.laboratorios_solicitados
            ):
                return False

            # Actualizar inventario
            self.salones_disponibles -= solicitud.programa_academico.salones_solicitados
            self.laboratorios_disponibles -= solicitud.programa_academico.laboratorios_solicitados

            # Crear asignación
            asignacion = {
                "solicitud_id": str(solicitud.id),
                "programa_id": str(solicitud.programa_academico.id),
                "salones_asignados": solicitud.programa_academico.salones_solicitados,
                "laboratorios_asignados": solicitud.programa_academico.laboratorios_solicitados,
                "fecha_asignacion": solicitud.fecha_solicitud.isoformat()
            }

            # Registrar asignación
            self.asignaciones.append(asignacion)
            solicitud.agregar_asignacion(asignacion)
            return True

    def liberar_aulas(self, solicitud: SolicitudAulas) -> bool:
        """Libera las aulas asignadas a una solicitud."""
        with self._lock:
            # Buscar la asignación
            asignacion = None
            for a in self.asignaciones:
                if a["solicitud_id"] == str(solicitud.id):
                    asignacion = a
                    break

            if not asignacion:
                return False

            # Devolver recursos al inventario
            self.salones_disponibles += asignacion["salones_asignados"]
            self.laboratorios_disponibles += asignacion["laboratorios_asignados"]

            # Eliminar asignación
            self.asignaciones.remove(asignacion)
            return True

    def notificar_asignacion_especial(self, solicitud: SolicitudAulas, mensaje: str) -> None:
        """Notifica sobre asignaciones especiales (aulas móviles)."""
        with self._lock:
            # Aquí se implementará la lógica de notificación
            # Por ahora solo registramos el mensaje
            print(f"Notificación especial para solicitud {solicitud.id}: {mensaje}")

    def obtener_estadisticas(self) -> Dict:
        """Obtiene estadísticas del gestor de recursos."""
        with self._lock:
            return {
                "salones_disponibles": self.salones_disponibles,
                "laboratorios_disponibles": self.laboratorios_disponibles,
                "total_asignaciones": len(self.asignaciones)
            }

    def __str__(self) -> str:
        return f"Gestor de Recursos (Salones: {self.salones_disponibles}, Laboratorios: {self.laboratorios_disponibles})"

    def __repr__(self) -> str:
        return f"GestorRecursos(salones={self.salones_disponibles}, laboratorios={self.laboratorios_disponibles})" 