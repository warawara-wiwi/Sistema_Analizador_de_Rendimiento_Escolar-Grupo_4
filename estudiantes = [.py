estudiantes = [
    {"nombre": "Ana", "notas": [6.5, 5.8, 7.0], "asistencia": 90},
    {"nombre": "Carlos", "notas": [4.0, 3.5, 5.1], "asistencia": 75},
    {"nombre": "Beatriz", "notas": [5.5, 6.2, 5.8], "asistencia": 88},
    {"nombre": "Diego", "notas": [3.0, 4.2, 2.8], "asistencia": 60},
    {"nombre": "Elena", "notas": [6.8, 7.0, 6.9], "asistencia": 95}
]



#PASO 2 : 

def aplicar_bono_asistencia(lista_con_promedios):
    """Paso 2: ajusta el promedio base segun la asistencia y guarda promedio_final."""
    """Ajusta el promedio segun asistencia y guarda el resultado en promedio_final."""
    for estudiante in lista_con_promedios:
        promedio_base = estudiante.get("promedio_base")

        if promedio_base is None:
            continue

        if estudiante.get("asistencia", 0) >= 90:
            promedio_ajustado = promedio_base + 0.3
        elif estudiante.get("asistencia", 0) < 70:
            promedio_ajustado = promedio_base - 0.2
        else:
            promedio_ajustado = promedio_base

        promedio_ajustado = max(1.0, min(7.0, promedio_ajustado))
        estudiante["promedio_final"] = round(promedio_ajustado, 1)

    return lista_con_promedios

#PASO 4 :

def calcular_metricas_globales(lista_clasificada):
    """Paso 4: calcula las metricas globales del curso a partir de la lista clasificada."""
    """Calcula metricas globales del curso a partir de la lista clasificada."""
    if not lista_clasificada:
        return {
            "promedio_general": 0.0,
            "total_aprobados": 0,
            "total_reprobados": 0
        }

    suma_promedios = 0.0
    total_promedios = 0
    total_aprobados = 0
    total_reprobados = 0

    for estudiante in lista_clasificada:
        promedio_final = estudiante.get("promedio_final")
        if isinstance(promedio_final, (int, float)):
            suma_promedios += promedio_final
            total_promedios += 1

        clasificacion = str(
            estudiante.get("clasificacion")
            or estudiante.get("estado")
            or ""
        ).lower()

        if "reprob" in clasificacion:
            total_reprobados += 1
        elif "aprob" in clasificacion:
            total_aprobados += 1
        elif isinstance(promedio_final, (int, float)):
            if promedio_final >= 4.0:
                total_aprobados += 1
            else:
                total_reprobados += 1

    promedio_general = round(suma_promedios / total_promedios, 1) if total_promedios else 0.0

    return {
        "promedio_general": promedio_general,
        "total_aprobados": total_aprobados,
        "total_reprobados": total_reprobados
    }


def generar_reporte_academia(lista_estudiantes):
    """Paso final: une todos los pasos y muestra un reporte limpio en pantalla."""
    # Paso 1: calcula los promedios base.
    # Si la funcion del Integrante 1 tiene otro nombre, reemplaza validar_y_obtener_promedios por ese nombre.
    lista_con_promedios = validar_y_obtener_promedios(lista_estudiantes)  # type: ignore[name-defined]

    # Paso 2: aplica el bono o descuento por asistencia.
    lista_con_bono = aplicar_bono_asistencia(lista_con_promedios)

    # Paso 3: clasifica a los estudiantes.
    # Si la funcion del Integrante 3 tiene otro nombre, reemplaza clasificar_estudiantes por ese nombre.
    lista_clasificada = clasificar_estudiantes(lista_con_bono)  # type: ignore[name-defined]

    # Paso 4: obtiene las metricas generales del curso.
    metricas = calcular_metricas_globales(lista_clasificada)

    # Paso 5: imprime el reporte final de forma ordenada.
    print("=== REPORTE DE RENDIMIENTO ACADEMIA ===")

    for estudiante in lista_clasificada:
        nombre = estudiante.get("nombre", "Sin nombre")
        promedio_final = estudiante.get("promedio_final", 0.0)
        clasificacion = estudiante.get("clasificacion") or estudiante.get("estado")

        if not clasificacion:
            if isinstance(promedio_final, (int, float)) and promedio_final >= 4.0:
                clasificacion = "Aprobado"
            else:
                clasificacion = "Reprobado"

        clasificacion_formateada = str(clasificacion).replace("_", " ").strip().title()
        print(f"- {nombre}: Promedio Final {promedio_final:.2f} -> {clasificacion_formateada}")

    print("=======================================")
    print("Métricas del Curso:")
    print(f"* Promedio General: {metricas['promedio_general']:.1f}")
    print(f"* Total Aprobados: {metricas['total_aprobados']}")
    print(f"* Total Reprobados: {metricas['total_reprobados']}")

    return {
        "estudiantes": lista_clasificada,
        "metricas": metricas
    }


