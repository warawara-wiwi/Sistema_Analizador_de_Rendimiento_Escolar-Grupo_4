estudiantes = [
    {"nombre": "Ana", "notas": [6.5, 5.8, 7.0], "asistencia": 90},
    {"nombre": "Carlos", "notas": [4.0, 3.5, 5.1], "asistencia": 75},
    {"nombre": "Beatriz", "notas": [5.5, 6.2, 5.8], "asistencia": 88},
    {"nombre": "Diego", "notas": [3.0, 4.2, 2.8], "asistencia": 60},
    {"nombre": "Elena", "notas": [6.8, 7.0, 6.9], "asistencia": 95}
]



#PASO 2 : 

def aplicar_bono_asistencia(lista_con_promedios):
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

