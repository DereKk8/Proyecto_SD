from typing import Dict, List
from facultad import Facultad
from programa_academico import ProgramaAcademico

def cargar_datos() -> Dict[str, Facultad]:
    """
    Carga los datos de facultades y programas desde el archivo de texto.
    Retorna un diccionario con las facultades y sus programas.
    """
    facultades = {}
    facultad_actual = None

    with open('database/facultades_programas.txt', 'r', encoding='utf-8') as file:
        for linea in file:
            linea = linea.strip()
            if not linea:  # Saltar líneas vacías
                continue

            if linea.startswith("Facultad"):
                # Crear nueva facultad
                facultad_actual = Facultad(nombre=linea)
                facultades[linea] = facultad_actual
            elif linea.startswith("Programa"):
                # Crear y agregar programa a la facultad actual
                programa = ProgramaAcademico(nombre=linea, facultad=facultad_actual.nombre)
                facultad_actual.agregar_programa(programa)

    return facultades

def listar_facultades() -> List[str]:
    """Retorna la lista de nombres de facultades."""
    return list(cargar_datos().keys())

def obtener_facultad(nombre: str) -> Facultad:
    """Obtiene una facultad por su nombre."""
    return cargar_datos().get(nombre)

def listar_programas_facultad(nombre_facultad: str) -> List[str]:
    """Retorna la lista de nombres de programas de una facultad."""
    facultad = obtener_facultad(nombre_facultad)
    if facultad:
        return [programa.nombre for programa in facultad.programas]
    return [] 