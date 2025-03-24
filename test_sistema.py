from cargador_datos import cargar_datos, obtener_facultad
from solicitud_aulas import SolicitudAulas

def test_sistema_asignacion():
    # 1. Cargar datos del sistema
    print("\nCargando datos del sistema...")
    facultades = cargar_datos()
    print(f"Total de facultades cargadas: {len(facultades)}")

    # 2. Obtener una facultad específica (por ejemplo, Ingeniería)
    facultad_ingenieria = obtener_facultad("Facultad de Ingeniería")
    print(f"\nFacultad seleccionada: {facultad_ingenieria}")

    # 3. Obtener un programa específico
    programa_sistemas = facultad_ingenieria.obtener_programa("Programa de Ingeniería de Sistemas")
    print(f"Programa seleccionado: {programa_sistemas}")

    # 4. Generar una solicitud de aulas
    print("\nGenerando solicitud de aulas...")
    solicitud = programa_sistemas.generar_solicitud(salones=3, laboratorios=2)
    print(f"Solicitud generada: {solicitud}")
    print(f"Salones solicitados: {programa_sistemas.salones_solicitados}")
    print(f"Laboratorios solicitados: {programa_sistemas.laboratorios_solicitados}")

    # 5. Procesar la solicitud
    print("\nProcesando solicitud...")
    solicitud.actualizar_estado("aprobada")
    print(f"Estado de la solicitud: {solicitud.estado}")

    # 6. Asignar aulas
    print("\nAsignando aulas...")
    asignacion = {
        "salon": "101",
        "tipo": "aula",
        "capacidad": 30
    }
    solicitud.agregar_asignacion(asignacion)
    print(f"Asignaciones realizadas: {solicitud.asignaciones}")

if __name__ == "__main__":
    test_sistema_asignacion() 