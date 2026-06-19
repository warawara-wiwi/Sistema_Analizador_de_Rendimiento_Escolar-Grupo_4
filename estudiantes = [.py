estudiantes = [
    {"nombre": "Ana", "notas": [6.5, 5.8, 7.0], "asistencia": 90},
    {"nombre": "Carlos", "notas": [4.0, 3.5, 5.1], "asistencia": 75},
    {"nombre": "Beatriz", "notas": [5.5, 6.2, 5.8], "asistencia": 88},
    {"nombre": "Diego", "notas": [3.0, 4.2, 2.8], "asistencia": 60},
    {"nombre": "Elena", "notas": [6.8, 7.0, 6.9], "asistencia": 95}
]

#PASO 3
def clasificar_estudiantes(lista_con_promedio_final):
    for estudiante in lista_con_promedio_final:
        promedio = estudiante["promedio_final"]
        
        if promedio >= 5.0:
            estudiante["estado"] = "Aprobado con Distinción"
        elif promedio >= 4.0:
            estudiante["estado"] = "Aprobado"
        else:
            estudiante["estado"] = "Reprobado"
    
    return lista_con_promedio_final
